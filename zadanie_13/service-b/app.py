from fastapi import FastAPI
import redis

app = FastAPI()

with open('/run/configs/redis_url', 'r') as f:
    redis_url = f.read().strip()
redis_client = redis.Redis.from_url(redis_url)

@app.get("/")
async def root():
    counter = redis_client.incr("request_counter")
    return {"counter": counter}

@app.get("/health")
async def health():
    return {"status": "healthy"}