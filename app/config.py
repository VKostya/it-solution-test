from pydantic import BaseSettings
import logging

class Config(BaseSettings):
    HOST: str
    PORT: int

    DATABASE_URL: str
    
    class Config:
        env_file = ".env"


config = Config()
logger = logging.getLogger(__name__)