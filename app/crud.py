import json
from sqlalchemy.orm import Session
from app.models import InvoiceRecord
from app.schemas import ExtractedInvoice
from app.logger import logger


def save_invoice_extraction(
    db: Session, extraction_data: ExtractedInvoice, raw_text: str
) -> InvoiceRecord:
    """Takes a validated Pydantic ExtractedInvoice schema object, serializes

    nested line items into a JSON string, and commits it securely to the local SQLite database.
    """
    logger.info(
        f"Preparing database write for vendor entry: '{extraction_data.vendor_name}'"
    )

    try:
        # Convert the complex Pydantic line items list into a flat, web-safe string format for database storage
        serialized_line_items = json.dumps(
            [item.model_dump() for item in extraction_data.line_items]
        )

        # Map our incoming data fields onto the SQLAlchemy Database Model columns
        db_record = InvoiceRecord(
            vendor_name=extraction_data.vendor_name,
            invoice_number=extraction_data.invoice_number,
            invoice_date=extraction_data.invoice_date,
            subtotal=extraction_data.subtotal,
            tax=extraction_data.tax,
            total_amount=extraction_data.total_amount,
            line_items_json=serialized_line_items,
            raw_source_text=raw_text,
        )

        # Stage and commit the transaction record safely inside SQLite
        db.add(db_record)
        db.commit()
        db.refresh(db_record)  # Populate the unique autoincremented database ID onto the object

        logger.info(
            f"Database record committed successfully. Generated Primary Key ID: {db_record.id}"
        )
        return db_record

    except Exception as db_write_error:
        db.rollback()  # Instantly abort the transaction to avoid database pool corruption
        logger.error(
            f"Database rollback executed. Failed to write record. Details: {str(db_write_error)}"
        )
        raise