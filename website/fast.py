from fastapi import Form, File, UploadFile, Request, FastAPI
from fastapi.staticfiles import StaticFiles
from typing import List
from fastapi.responses import ORJSONResponse
from fastapi.templating import Jinja2Templates
import subprocess

app = FastAPI()
templates = Jinja2Templates(directory="templates")

#In python assigning a variable with type it can be defined with a colon like below 
@app.post("/submit")
def submit(
        contact:  str = Form(""),
        proxy1: str = Form(""),
        proxy2: str = Form(""),
        proxy3: str = Form(""),
        proxy4: str = Form(""),
        fname1: str = Form(""),
        fname2: str = Form(""),
        fname3: str = Form(""),
        fname4: str = Form(""),
        text5: str = Form("")
):
   print("radio: " + contact, "\nCheckbox: " + proxy1, "\ncheckbox" + proxy1,
         "\ncheckbox" + proxy2, "\ncheckbox" + proxy3, "\ncheckbox" + proxy4, 
         "\ntext" + fname1, "\ntext" + fname2, "\ntext" + fname3, "\ntext" + fname4, "\ntext5 : " + text5)

app.mount("/", StaticFiles(directory="templates",html = True), name="templates")