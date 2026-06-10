from datetime import datetime
from sqlalchemy import String, Float, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class InvoiceRecord(Base):
    """Declarative SQLAlchemy table configuration mapping out the long-term

    relational storage matrix for extracted financial documents.
    """

    __tablename__ = "invoice_records"

    # Primary key and core structural metadata fields
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    processed_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    # Core high-level invoice parameters extracted by the AI engine
    vendor_name: Mapped[str] = mapped_column(String(255), nullable=False)
    invoice_number: Mapped[str] = mapped_column(
        String(100), default="UNKNOWN", nullable=False
    )
    invoice_date: Mapped[str] = mapped_column(
        String(50), default="UNKNOWN", nullable=False
    )

    # Financial Summary Metrics
    subtotal: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    tax: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    total_amount: Mapped[float] = mapped_column(
        Float, default=0.0, nullable=False
    )

    # Deep Storage: Serialize full item breakdowns and raw texts for safety audits
    line_items_json: Mapped[str] = mapped_column(
        Text, nullable=False
    )  # Stores serialized list arrays
    raw_source_text: Mapped[str] = mapped_column(
        Text, nullable=False
    )  # Traceability backup