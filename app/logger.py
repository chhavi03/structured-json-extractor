import logging
import sys
from app.config import settings


def setup_logger(name: str = "structured-extractor") -> logging.Logger:
    """Configures and returns a unified, structured logger instance.

    Sets severity levels based on the application environment and formats
    output to cleanly display timestamps, severity levels, and execution source.
    """
    logger = logging.getLogger(name)

    # Prevent duplicating handlers if this function is called multiple times
    if logger.handlers:
        return logger

    # Set logging level based on environment
    if settings.APP_ENV == "production":
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.DEBUG)

    # Create a clean, human-readable terminal format
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Direct log outputs straight to standard streams
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


# Instantiate a singleton logger for the application
logger = setup_logger()