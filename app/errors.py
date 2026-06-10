from typing import Any, Dict, Optional


class AppError(Exception):
    """Base exception class for all custom application errors.

    Provides standard properties for machine-readable error codes and
    sanitized, user-friendly messages.
    """

    def __init__(
        self,
        message: str,
        code: str = "INTERNAL_SERVER_ERROR",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}


class ConfigurationError(AppError):
    """Raised when environment variables or vital settings are misconfigured."""

    def __init__(
        self, 
        message: str, 
        details: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(message, code="CONFIGURATION_ERROR", details=details)


class DocumentParsingError(AppError):
    """Raised when the text extraction pipeline fails to parse a document."""

    def __init__(
        self, 
        message: str, 
        details: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(message, code="DOCUMENT_PARSING_ERROR", details=details)


class LLMOrchestrationError(AppError):
    """Raised when communication with the LLM API provider fails or times out."""

    def __init__(
        self, 
        message: str, 
        details: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(message, code="LLM_ORCHESTRATION_ERROR", details=details)