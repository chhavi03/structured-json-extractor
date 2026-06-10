from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings
from app.logger import logger

# 1. Define the Base architectural class using modern SQLAlchemy 2.0 syntax
# This class must exist at the module level so Python can always import it cleanly.
class Base(DeclarativeBase):
    pass

try:
    # 2. Create the master Engine using the connection string from config.py
    engine = create_engine(
        settings.DATABASE_URL, connect_args={"check_same_thread": False}
    )

    # 3. Establish a Sessionmaker factory to spawn distinct transactional database sessions
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    logger.info("Database orchestration engine initialized successfully.")

except Exception as db_init_error:
    logger.critical(
        f"Critical Failure: Unable to bind database engine to target URL. Details: {str(db_init_error)}"
    )
    raise