import time
from typing import Dict
import os
import binascii
import jwt
from decouple import config

JWT_SECRET = config('secret')
JWT_ALGORITHM = config('algorithm')

def token_response(token:str):
    return {
        'access token':token
    }

def sign_jwt(user_id:str)->Dict[str,str]:
    payload = {
        'user_id': user_id,
        # 10 minutes time
        'expires': time.time()+600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}