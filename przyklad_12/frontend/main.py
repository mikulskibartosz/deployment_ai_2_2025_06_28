from fastapi import FastAPI
from datetime import datetime
import httpx

app = FastAPI()

@app.get("/ping")
async def ping():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://backend:8000/ping")
        backend_data = response.json()

    current_time = datetime.now().isoformat()

    return {
        "time": current_time,
        "backend_data": backend_data
    }