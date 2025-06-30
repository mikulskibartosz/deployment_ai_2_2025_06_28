from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import StreamingResponse
import string
import secrets
import time
import asyncio

app = FastAPI()

def generate_password_sync(length: int = 12) -> str:
    time.sleep(5)
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

async def generate_password_async(length: int = 12) -> str:
    await asyncio.sleep(5)
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


async def send_email(email: str, password: str):
    await asyncio.sleep(5)
    print(f"Sending email to {email} with password {password}")


async def password_stream():
    count = 0
    while count < 10:
        password = await generate_password_async()
        yield f"Password {count}: {password}"
        count += 1
        await asyncio.sleep(1)

@app.get("/sync")
def sync_password():
    return {"password": generate_password_sync()}

@app.get("/async")
async def async_password():
    password1 = generate_password_async()
    password2 = generate_password_async()
    password1, password2 = await asyncio.gather(password1, password2)
    return {"password1": password1, "password2": password2}

@app.get("/background")
async def background_password(background_tasks: BackgroundTasks):
    password1 = generate_password_async()
    password = await password1
    background_tasks.add_task(send_email, "test@test.com", password)
    return {"password": password}

@app.get("/stream")
async def stream_password():
    return StreamingResponse(password_stream(), media_type="text/event-stream")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)