from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/ping")
async def ping():
    with open("summary.json", "r") as f:
        summary = json.load(f)

    try:
        import pandas as pd
        summary["pandas_installed"] = True
    except ImportError:
        summary["pandas_installed"] = False

    return summary
