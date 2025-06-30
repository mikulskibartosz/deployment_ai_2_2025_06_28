from fastapi import FastAPI
from datetime import datetime
import httpx

app = FastAPI()

@app.get("/ping")
async def ping():

    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/ping")
        respone_json = response.json()

    return {"time": datetime.now().isoformat(), "service": "B", "response": respone_json}
