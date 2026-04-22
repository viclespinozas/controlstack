from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://db:27017"
    DATABASE_NAME: str = "controlstack"

settings = Settings()