import os
from typing import Optional
from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get('/healthcheck')
async def healthcheck():
    return {"result": "alive"}

@app.get('/')
async def main():
    return {"ready":True}

@app.get('/authorized')
async def authorized():
    return {"authorized":True}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")