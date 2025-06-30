from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI()

@app.get("/ping")
async def ping():
    current_time = datetime.now().isoformat()
    sages_env = os.getenv("SAGES_ENV")
    override_env = os.getenv("OVERRIDE_ENV")
    run_env = os.getenv("RUN_ENV")
    return {"time": current_time, "sages_env": sages_env, "override_env": override_env, "run_env": run_env}
