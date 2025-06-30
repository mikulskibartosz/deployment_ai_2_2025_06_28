from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()
client = httpx.AsyncClient()

@app.get("/")
async def root():
    responses = await asyncio.gather(
        client.get("http://service-b:8000/"),
        client.get("http://service-c:8000/")
    )

    return {
        "counter": responses[0].json(),
        "uuid": responses[1].json()
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}