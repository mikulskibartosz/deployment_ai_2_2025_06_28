from fastapi import FastAPI
from datetime import datetime
import json

# Zmiany w pliku docker-compose.yaml oraz kodzie Pythona:

# użyj parametru configs do przekazania zawartości pliku, wartości tekstowej, oraz wartości ze zmiennej środowiskowej do kontenera
# użyj parameters secrets do przekazania nazwy pliku do kontenera
# zamontuj lokalny katalog w kontenerze
# w zamontowanym katalogu utwórz plik mający taką samą nazwę jak wartość przekazanego sekretu
# zawartością pliku powinny bye wartości z przekazanej konfiguracji

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

    with open("/run/secrets/nazwa_pliku", "r", encoding="utf-8") as f:
        nazwa_pliku = f.read()

    config_dictionary = {
        "config": config,
        "tekst": tekst,
        "zmienna": zmienna
    }

    with open(f"/katalog/{nazwa_pliku}", "w", encoding="utf-8") as f:
        f.write(json.dumps(config_dictionary))

    return {"time": current_time, "config": config, "tekst": tekst, "zmienna": zmienna, "nazwa_pliku": nazwa_pliku}
