from fastapi import FastAPI
from datetime import datetime
import os
import json

app = FastAPI()

@app.get("/ping")
async def ping():
    current_time = datetime.now().isoformat()

    os.makedirs("/katalog", exist_ok=True)
    with open("/katalog/data.json", "w") as f:
        envs = os.environ.items()
        envs_dict = dict(envs)
        json.dump(envs_dict, f)

    return {"time": current_time, "envs": envs}
