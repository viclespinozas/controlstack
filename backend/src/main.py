from src.database import db
from fastapi import FastAPI

app = FastAPI(title="ControlStack API")

@app.get("/")
async def root():
    return {"message": "FastAPI ControlStack is alive"}

@app.get("/health")
async def health():
    try:
        # Ping MongoDB
        await db.command("ping")
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        return {"status": "error", "db_error": str(e)}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
