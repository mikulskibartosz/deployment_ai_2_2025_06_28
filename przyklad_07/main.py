from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI()

@app.get("/ping")
async def ping():
    current_time = datetime.now().isoformat()

    env_variable = os.getenv("ENV_VARIABLE", "default")

    with open("/data/data.txt", "w") as f:
        f.write(current_time)
        f.write(env_variable)

    with open("/sages/data.txt", "w") as f:
        f.write(current_time)
        f.write(env_variable)

    with open("/inny/data.txt", "w") as f:
        f.write(current_time)
        f.write(env_variable)

    return {"time": current_time, "env_variable": env_variable}
