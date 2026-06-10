from app.database import engine, Base
from app.logger import logger
# We must import models here so that Base knows InvoiceRecord exists
from app import models 

def initialize_database():
    """Reads all compiled SQLAlchemy models and generates the physical 

    database tables on disk if they do not already exist.
    """
    logger.info("Initializing physical database tables...")
    try:
        # This single line looks at Base, finds all tables, and creates them in SQLite
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables generated and verified successfully.")
    except Exception as raw_db_error:
        logger.error(f"Failed to generate physical database: {str(raw_db_error)}")
        raise

if __name__ == "__main__":
    initialize_database()