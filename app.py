from fastapi import FastAPI

app = FastAPI()


@app.post("/login")
async def login(username: str, password: str):
    return {"username": username}
