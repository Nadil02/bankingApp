import jwt
import datetime
import os
from dotenv import load_dotenv
from fastapi import HTTPException

#load_secret_key_from_env
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY","secret_key")
ALGORITHM = "HS256"

ACCESS_TOKEN_EXP_MIN= 15 #used_for_authentication_in_API_requests
REFRESH_TOKEN_DAYS=1 #used_to_generate_new_access_token_without_loggin_in_again

#generate_jwt_token
def create_jwt(data: dict, expired_delta: int = ACCESS_TOKEN_EXP_MIN):
    
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=expired_delta)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

#generate_refresh_token
def create_refresh_token(data: dict):
    return create_jwt(data, expired_delta=REFRESH_TOKEN_DAYS*24*60)

def verify_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload #valid_token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token Expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid Token")

