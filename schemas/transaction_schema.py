from pydantic import BaseModel
from typing import Optional

class TransactionCreate(BaseModel):
    name: str
    description: Optional[str] = None

class TransactionUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class TransactionResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None