from fastapi import FastAPI
import redis

app = FastAPI()

redis_client = redis.Redis(host="redis", port=6379, db=0)

@app.get("/ping")
async def ping():
    licznik = redis_client.incr("ping_counter")
    return {"licznik": licznik}