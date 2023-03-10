import FastAPI

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