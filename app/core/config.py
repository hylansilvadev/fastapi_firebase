from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', env_ignore_empty=True
    )

    SECRET_DATABASE_PATH: str


settings = Settings()
