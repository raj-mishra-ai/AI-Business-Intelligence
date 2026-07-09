from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    PROJECT_NAME: str
    PROJECT_VERSION: str

    class Config:
        env_file = "app/.env"


settings = Settings()