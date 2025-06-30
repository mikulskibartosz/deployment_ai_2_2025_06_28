from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI()

random_number = random.randint(0, 10000)

@app.get("/ping")
async def ping():
    return {"time": datetime.now().isoformat(), "service": "A", "random_number": random_number}
