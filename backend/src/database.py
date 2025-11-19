import motor.motor_asyncio
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://db:27017")
DB_NAME = os.getenv("MONGO_DB", "controlstack")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
