from pydantic import BaseSettings
import logging

class Config(BaseSettings):
    HOST: str
    PORT: int
    class Config:
        env_file = ".env"


config = Config()
logger = logging.getLogger(__name__)