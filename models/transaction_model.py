from pydantic import BaseModel
from typing import Optional

class Transaction(BaseModel):
    id: str
    name: str
    description: Optional[str]