from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/ping")
async def ping():
    current_time = datetime.now().isoformat()

    with open("/config/config.xml", "r", encoding="utf-8") as f:
        config = f.read()

    with open("/config/tekst.txt", "r", encoding="utf-8") as f:
        tekst = f.read()

    with open("/config/zmienna", "r", encoding="utf-8") as f:
        zmienna = f.read()

    with open("/run/secrets/token", "r", encoding="utf-8") as f:
        token = f.read()

    with open("/run/secrets/certyfikat", "r", encoding="utf-8") as f:
        certyfikat = f.read()

    return {"time": current_time, "config": config, "tekst": tekst, "zmienna": zmienna, "token": token, "certyfikat": certyfikat}
