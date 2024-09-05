from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="static",html = True), name="static")

@app.get("/items/{y}/{item_id}")
async def read_item(item_id: int, y):
    return {"item_id": item_id}