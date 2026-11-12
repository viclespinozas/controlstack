from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from core.database import get_db
from routes.transaction_routes import router as transaction_router

app = FastAPI(title="Control Stack API")

app.include_router(transaction_router)

@app.get("/health")
async def health(db: AsyncSession = Depends(get_db)):
    await db.execute(text("SELECT 1"))
    return {"status": "connected"}