import instructor
import google.generativeai as genai
from app.config import settings
from app.errors import LLMOrchestrationError
from app.logger import logger
from app.schemas import ExtractedInvoice


def extract_structured_data(document_text: str) -> ExtractedInvoice:
    """Sends raw document text to the Gemini AI platform using the legacy google-generativeai SDK
    wrapped by instructor and forces it to return a validated ExtractedInvoice data object.
    """
    logger.info("Initiating structured data extraction with Gemini platform...")

    try:
        # Configure the legacy google-generativeai SDK with the Google API Key
        genai.configure(api_key=settings.GOOGLE_API_KEY)

        # Wrap it with instructor using from_gemini mapping to the specific model and Mode.GEMINI_JSON
        client = instructor.from_gemini(
            client=genai.GenerativeModel(
                model_name="models/gemini-flash-latest"
            ),
            mode=instructor.Mode.GEMINI_JSON,
        )

        # Execute the structured extraction request using chat.completions.create
        response = client.chat.completions.create(
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