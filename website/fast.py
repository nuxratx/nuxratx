from fastapi import Form, File, UploadFile, Request, FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from typing import List
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import subprocess


app = FastAPI()
templates = Jinja2Templates(directory="templates")

#In python assigning a variable with type it can be defined with a colon like below 

class Base(BaseModel):
        contact: str | None
        proxy1: str | None
        proxy2: str | None
        proxy3: str | None
        proxy4: str | None
        fname1: str | None
        fname2: str | None
        fname3: str | None
        fname4: str | None
        text5: str | None
    


@app.post("/submit")
def submit(base: Base = Depends()):
   return base

app.mount("/", StaticFiles(directory="templates",html = True), name="templates")

@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})