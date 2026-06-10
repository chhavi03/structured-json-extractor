import instructor
from google import genai
from app.config import settings
from app.errors import LLMOrchestrationError
from app.logger import logger
from app.schemas import ExtractedInvoice


def extract_structured_data(document_text: str) -> ExtractedInvoice:
    """Sends raw document text to the Gemini AI platform using the modern genai SDK

    and forces it to return a validated ExtractedInvoice data object.
    """
    logger.info("Initiating structured data extraction with Gemini platform...")

    try:
        # Initialize the modern, official Google GenAI Client natively with your settings key
        genai_client = genai.Client(api_key=settings.GEMINI_API_KEY)

        # Wrap it with instructor using the modern from_genai routing engine
        client = instructor.from_genai(genai_client, mode=instructor.Mode.GENAI_TOOLS)

        # Execute the structured extraction request
        response = client.chat.completions.create(
            model="gemini-1.5-flash",
            messages=[
                {
                    "role": "user",
                    "content": f"Analyze the following raw text extracted from an invoice. "
                    f"Extract all required details exactly according to the schema rules.\n\n"
                    f"RAW INVOICE TEXT:\n{document_text}",
                }
            ],
            response_model=ExtractedInvoice,
        )

        logger.info("Data extraction completed and validated successfully.")
        return response

    except Exception as raw_error:
        logger.error(f"LLM Orchestration failure encountered: {str(raw_error)}")
        raise LLMOrchestrationError(
            message="The AI engine failed to analyze and extract data from the document text.",
            details={"system_exception": str(raw_error)},
        )