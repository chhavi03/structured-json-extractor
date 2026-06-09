import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Enterprise configuration management utilizing Pydantic Settings.

    Automatically parses environmental variables from the system or a local
    .env file, applying strict data validation rules at startup.
    """

    # LLM API Keys
    OPENAI_API_KEY: str = Field(default="mock-key-for-testing")
    ANTHROPIC_API_KEY: str = Field(default="mock-key-for-testing")

    # Application Settings
    APP_ENV: str = Field(default="development")
    DATABASE_URL: str = Field(default="sqlite:///./extraction_logs.db")

    # Target the parent directory's .env file
    model_config = SettingsConfigDict(
        env_file=os.path.join(
            os.path.dirname(os.path.dirname(__file__)), ".env"
        ),
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()