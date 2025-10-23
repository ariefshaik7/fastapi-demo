from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # This tells pydantic to load from a .env file
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Define your settings
    DATABASE_URL: str


# Create a single, cached instance of the settings
settings = Settings()
