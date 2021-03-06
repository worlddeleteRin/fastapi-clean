from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Some app name"
    JWT_SECRET_KEY: str = ''
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 1
    JWT_SESSION_KEY: str = ''
    JWT_SESSION_TOKEN_EXPIRE_MINUTES: int = 1
    JWT_ALGORITHM: str = "HS256"
    DB_URL: str = ''
    DB_NAME: str = ''
    DEBUG_MODE: bool = True
    # base static url
    base_static_url: str = ""



    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    print('execute get_settings function')
    return Settings()

settings = get_settings()
