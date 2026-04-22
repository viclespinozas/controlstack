from core.database import db
from bson import ObjectId

class TransactionRepository:
    collection = db["transactions"]

    async def create(self, data: dict) -> str:
        result = await self.collection.insert_one(data)
        return str(result.inserted_id)

    async def get_all(self):
        cursor = self.collection.find({})
        return [self._serialize(doc) async for doc in cursor]

    async def get_by_id(self, transaction_id: str):
        doc = await self.collection.find_one({"_id": ObjectId(transaction_id)})
        return self._serialize(doc) if doc else None

    async def update(self, transaction_id: str, data: dict):
        await self.collection.update_one({"_id": ObjectId(transaction_id)}, {"$set": data})
        return await self.get_by_id(transaction_id)

    async def delete(self, transaction_id: str):
        await self.collection.delete_one({"_id": ObjectId(transaction_id)})

    @staticmethod
    def _serialize(doc):
        return {**doc, "id": str(doc["_id"])} if doc else None