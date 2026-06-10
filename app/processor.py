import os
from pypdf import PdfReader
from app.errors import DocumentParsingError
from app.logger import logger


def extract_text_from_pdf(file_path: str) -> str:
    """Opens a local PDF file, loops through its pages, extracts all visible

    text, and returns it as a single consolidated string.
    """
    logger.info(f"Targeting file for processing pipeline: '{file_path}'")

    # Safety Check: Verify the file actually exists on disk
    if not os.path.exists(file_path):
        logger.error(f"File target mismatch: Path '{file_path}' does not exist.")
        raise DocumentParsingError(
            message=f"The system could not locate the specified file at: {file_path}"
        )

    try:
        # Initialize the pypdf file reader
        reader = PdfReader(file_path)
        extracted_segments = []

        # Loop through pages sequentially and pull structural text layers
        for page_index, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                extracted_segments.append(page_text)

        # Merge all pages together into a unified text document
        full_text = "\n".join(extracted_segments).strip()

        # Safety Check: If no text could be extracted, throw a custom parsing exception
        if not full_text:
            logger.error(f"Extraction void: Zero string layers resolved from '{file_path}'")
            raise DocumentParsingError(
                message="The document was read successfully, but it appears to be entirely blank or unreadable scanned imagery."
            )

        logger.info(
            f"Extraction pipe complete. Captured {len(full_text)} characters from document."
        )
        return full_text

    except DocumentParsingError:
        # Re-raise our deliberate structural checks so they skip global capture
        raise
    except Exception as raw_system_error:
        # Trap generic file system library crashes (like corrupted binaries)
        logger.error(f"Binary parsing crash encountered: {str(raw_system_error)}")
        raise DocumentParsingError(
            message="Failed to parse the physical document layers due to an underlying file corruption.",
            details={"system_exception": str(raw_system_error)},
        )