from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    MODE: Literal["DEV", "TEST", "PROD"] = "DEV"

    DB_NAME: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str

    TEST_DB_NAME: str
    TEST_DB_PASS: str
    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_USER: str

    ADMIN_EMAIL: str
    ADMIN_PASS: str

    SECRET_KEY_JWT: str
    ALGORITM: str

    @property
    def db_connect(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def test_db_connect(self):
        return f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"


settings = Settings()
