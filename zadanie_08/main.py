from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/ping")
async def ping():
    current_time = datetime.now().isoformat()
    return {"time": current_time}
