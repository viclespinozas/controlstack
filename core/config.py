import os

class Settings():
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://db:27017")
    DATABASE_NAME = os.getenv("MONGO_DB", "controlstack")

settings = Settings()