from fastapi import FastAPI, Path
import uvicorn
app = FastAPI()

@app.get('/')
async def root():
    return {'message' : 'rohan'}

@app.get('/hello/{name}')
async def hello(name):
    return name

@app.get("/data/{name}/{age}")
async def data(name:str=Path(max_length=5, min_length=3),age:int=Path(gt=18)):
   return {"name": name, "age":age} 


# use for validations at run time
from typing import List
from pydantic import BaseModel, Field
#field for metadata and validation

class Student(BaseModel):
    id : int
    name : str = Field(None, title="Descritpion", max_length=10)
    subjects : List[str] =[]


@app.post('/students')
async def student_data(s1:Student):
    return s1


# templates
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get('/template/{name}')
async def template(request:Request, name:str):
    return templates.TemplateResponse('index.html', {'request':request, 'name':name})

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)