from fastapi import FastAPI
from datetime import datetime
import time
import random

app = FastAPI()

start_time = time.time()
max_time = 60

@app.get("/ping")
async def ping():
    elapsed_seconds = time.time() - start_time
    failure_probability = min(1.0, elapsed_seconds / max_time)

    should_fail = random.random() < failure_probability

    if should_fail:
        raise Exception("Fail")

    return {"time": datetime.now().isoformat()}
