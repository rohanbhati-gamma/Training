from fastapi import FastAPI, Body, Depends

from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import sign_jwt
from app.model import PostSchema, UserSchema, UserLoginSchema

app = FastAPI()

@app.get('/',tags=['root'])
async def read_root()->dict:
    return {"message":"Welcome to Page"}

@app.get('/posts',tags=['posts'])
async def get_posts()->dict:
    return {'data':posts}

@app.get('/posts/{id}', tags=['posts'])
async def get_single_post(id:int)->dict:
    if id>len(posts):
        return {'error': 'NO such post exist'}
    for post in posts:
        if post['id']==id:
            return{
                'data':post
            }

@app.post('user/signup', tags=['user'])
async def create_user(user:UserSchema = Body(...)):
    users.append(user)
    return sign_jwt(user.email)

@app.post('/posts',dependencies=[Depends(JWTBearer())], tags=['posts'])
async def add_post(post:PostSchema)->dict:
    post.id = len(posts)+1
    posts.append(post.dict())
    return {'data':'post added'}

def check_user(data:UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return sign_jwt(user.email)
    return {
        "error": "Wrong login details!"
    }

posts = [
    {
        'id':1,
        'title':'Demo',
        'content':'Firs Post'
    }
]

users = []