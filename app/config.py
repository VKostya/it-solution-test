from pydantic import BaseSettings
import logging
import os


class Config(BaseSettings):
    HOST: str = os.getenv("HOST")
    PORT: int = os.getenv("PORT")

    DATABASE_URL: str = os.getenv("DATABASE_URL")

    class Config:
        env_file = ".env"


config = Config()
logger = logging.getLogger(__name__)
