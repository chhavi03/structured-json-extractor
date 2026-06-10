from typing import List, Optional
from pydantic import BaseModel, Field


class InvoiceItem(BaseModel):
    """Blueprint for a single line item inside an invoice."""

    description: str = Field(
        description="The clear name or description of the product or service purchased."
    )
    quantity: int = Field(
        description="The number of units purchased. Must be a whole number."
    )
    unit_price: float = Field(
        description="The cost per individual unit of this specific item."
    )
    total_amount: float = Field(
        description="The final total cost for this item line (quantity multiplied by unit_price)."
    )


class ExtractedInvoice(BaseModel):
    """The master data contract blueprint for the entire extracted invoice."""

    vendor_name: str = Field(
        description="The official name of the company or merchant issuing the invoice."
    )
    invoice_date: Optional[str] = Field(
        default=None,
        description="The date the invoice was issued, preferably formatted as YYYY-MM-DD if available.",
    )
    invoice_number: Optional[str] = Field(
        default=None,
        description="The unique identification number printed on the invoice document.",
    )
    line_items: List[InvoiceItem] = Field(
        description="A complete list of all individual products or services detailed in the invoice."
    )
    subtotal: float = Field(
        description="The calculated sum of all line items before taxes or shipping fees are added."
    )
    tax_amount: float = Field(
        default=0.0,
        description="The total tax amount charged on this invoice. Default to 0.0 if not specified.",
    )
    grand_total: float = Field(
        description="The final total amount due for payment, including taxes and fees."
    )