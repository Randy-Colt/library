from os import getenv

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    db_url: str = getenv('DB_URL', 'sqlite+aiosqlite:///../data/db.sqlite3')
    db_echo: bool = getenv('DB_ECHO', False)
    debug: bool = getenv('DEBUG', False)


settings = Settings()
