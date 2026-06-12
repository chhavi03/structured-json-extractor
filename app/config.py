import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Enterprise configuration management utilizing Pydantic Settings.

    Automatically parses environmental variables from the system or a local
    .env file, applying strict data validation rules at startup.
    """

    # LLM API Keys
    GOOGLE_API_KEY: str = Field(default="")
    GEMINI_API_KEY: str = Field(default="")
    OPENAI_API_KEY: str = Field(default="mock-key-for-testing")
    ANTHROPIC_API_KEY: str = Field(default="mock-key-for-testing")

    # Application Settings
    APP_ENV: str = Field(default="development")
    DATABASE_URL: str = Field(default="sqlite:///database.db")

    # Target the parent directory's .env file
    model_config = SettingsConfigDict(
        env_file=os.path.join(
            os.path.dirname(os.path.dirname(__file__)), ".env"
        ),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    def model_post_init(self, __context):
        # Fallback to GEMINI_API_KEY if GOOGLE_API_KEY is not explicitly set in environment or env file
        if not self.GOOGLE_API_KEY and self.GEMINI_API_KEY:
            self.GOOGLE_API_KEY = self.GEMINI_API_KEY


settings = Settings()