import google.generativeai as genai
import instructor
from app.config import settings
from app.errors import LLMOrchestrationError
from app.logger import logger
from app.schemas import ExtractedInvoice

# Configure the underlying Google Gemini SDK with your secure API key
genai.configure(api_key=settings.GEMINI_API_KEY)


def extract_structured_data(document_text: str) -> ExtractedInvoice:
    """Sends raw document text to the Gemini AI platform and forces it to

    return a perfectly structured, validated ExtractedInvoice data object.
    """
    logger.info("Initiating structured data extraction with Gemini platform...")

    try:
        # Wrap the standard Gemini client with instructor to enable Pydantic forcing
        client = instructor.from_gemini(
            client=genai.GenerativeModel(
                model_name="gemini-1.5-flash",
            ),
            mode=instructor.Mode.GEMINI_JSON,
        )

        # Execute the request to the AI provider
        response = client.messages.create(
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
        # Wrap any unexpected AI failure into our custom domain error tracker
        logger.error(f"LLM Orchestration failure encountered: {str(raw_error)}")
        raise LLMOrchestrationError(
            message="The AI engine failed to analyze and extract data from the document text.",
            details={"system_exception": str(raw_error)},
        )