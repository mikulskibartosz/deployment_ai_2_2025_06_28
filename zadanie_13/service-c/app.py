from fastapi import FastAPI
import redis
import uuid
import os

app = FastAPI()

with open('/run/secrets/redis_c_url', 'r') as f:
    redis_url = f.read().strip()
redis_client = redis.Redis.from_url(redis_url)

@app.get("/")
async def root():
    new_uuid = str(uuid.uuid4())
    redis_client.set("last_uuid", new_uuid)
    return {"uuid": new_uuid}

@app.get("/health")
async def health():
    return {"status": "healthy"}