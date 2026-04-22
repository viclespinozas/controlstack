from repositories.transaction_repo import TransactionRepository
from models.transaction_model import Item

class TransactionService:
    def __init__(self, repo: TransactionRepository):
        self.repo = repo

    async def create_transaction(self, payload):
        new_id = await self.repo.create(payload)
        return await self.repo.get_by_id(new_id)

    async def list_transactions(self):
        return await self.repo.get_all()

    async def get_transaction(self, transaction_id: str):
        return await self.repo.get_by_id(transaction_id)

    async def update_transaction(self, transaction_id: str, payload):
        return await self.repo.update(transaction_id, payload)

    async def delete_transaction(self, transaction_id: str):
        await self.repo.delete(transaction_id)
        return True