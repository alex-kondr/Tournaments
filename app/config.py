from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_uri: str = "mysql+aiomysql://avnadmin:AVNS_3-yt9ee4lQSFabtFpzi@mysql-31182646-alex-kondr.j.aivencloud.com:13316/tornaments"
    secret_key: str = "super secret key"
    exp_time_minutes: int = 30


settings = Settings()