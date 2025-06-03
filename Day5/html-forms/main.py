from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
import uvicorn
from fastapi import Form

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get('/')
async def home():
    return 'Home Page'

@app.get('/login',response_class=HTMLResponse)
async def login(request:Request):
    return templates.TemplateResponse('index.html',{'request':request})

from pydantic import BaseModel
class User(BaseModel):
   username:str
   password:str
@app.post("/submit/", response_model=User)
async def submit(nm: str = Form(...), pwd: str = Form(...)):
   return User(username=nm, password=pwd)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8001, reload=True)