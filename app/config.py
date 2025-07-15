from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_uri: str = "mysql+aiomysql://localhost:5432/tornaments"
    secret_key: str = "super secret key"
    exp_time_minutes: int = 30


settings = Settings()
