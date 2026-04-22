from fastapi import APIRouter, HTTPException
from schemas.transaction_schema import TransactionCreate, TransactionUpdate, TransactionResponse
from services.transaction_service import TransactionService
from repositories.transaction_repo import TransactionRepository

router = APIRouter(prefix="/transactions", tags=["Transactions"])

service = TransactionService(TransactionRepository())

@router.post("/", response_model=TransactionResponse)
async def create_transaction(payload: TransactionCreate):
    return await service.create_item(payload.dict())

@router.get("/", response_model=list[TransactionResponse])
async def list_transactions():
    return await service.list_transactions()

@router.get("/{transaction_id}", response_model=TransactionResponse)
async def get_transaction(transaction_id: str):
    transaction = await service.get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(404, "Transaction not found")
    return transaction

@router.put("/{transaction_id}", response_model=TransactionResponse)
async def update_transaction(transaction_id: str, payload: TransactionUpdate):
    return await service.update_transaction(transaction_id, payload.dict(exclude_none=True))

@router.delete("/{transaction_id}")
async def delete_transaction(transaction_id: str):
    await service.delete_transaction(transaction_id)
    return {"status": "deleted"}