from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    ig_user_id: str
    ig_access_token: str
    ig_api_version: str
    cat_image_api_url: str
    cat_image_api_key: str
    cat_fact_api_url: str


@lru_cache
def get_settings() -> Settings:
    return Settings()
