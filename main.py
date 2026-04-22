from fastapi import FastAPI
from routes.transaction_routes import router as transaction_router

app = FastAPI(title="My API")

app.include_router(transaction_router)