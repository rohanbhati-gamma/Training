from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Securing FastAPI applications with JWT.",
                "content": "In this tutorial, you'll learn how to secure your application by enabling authentication using JWT. We'll be using PyJWT to sign, encode and decode JWT tokens...."
            }
        }

class UserSchema(BaseModel):
    fullname: str= Field(...)
    email : EmailStr = Field(...)
    password : str = Field(...)

    class Config:
        json_schema_extra = {
            'fullname' : 'rohan bhati',
            'email' : 'rohan@gmail.com',
            'password' : '1234'
        }


class UserLoginSchema(BaseModel):
    email : EmailStr = Field(...)
    password : str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "rohan@gmail.com",
                "password": "1234"
            }
        }