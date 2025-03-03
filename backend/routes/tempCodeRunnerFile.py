from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
import motor.motor_asyncio
import os
from dotenv import load_dotenv
import jwt as pyjwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from pydantic import BaseModel

# load environment variables from .env file
load_dotenv()

# MongoDB URI from .env file
MONGO_URI = os.getenv("MONGO_URI")

# create a client instance for MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

# database
db = client["project"] 

# collections
collection_user = db["user"]

# Pydantic model
class userlogin(BaseModel):
    NIC: str
    passcode: str 

# Secret key and algorithm for JWT
SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXP_MIN = int(os.getenv("ACCESS_TOKEN_EXP_MIN", 15))  # Expiry in minutes
REFRESH_TOKEN_DAYS = 1  # Used to generate new access token without logging in again

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# MongoDB ObjectId conversion to string
def fix_mongo_id(document):
    if document and "_id" in document:
        document["_id"] = str(document["_id"])
    return document

# Hash the password before storing it in DB
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verify input password with hashed password from DB
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# JWT creation functions
def create_jwt(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXP_MIN)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return pyjwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict):
    return create_jwt(data, expires_delta=timedelta(days=REFRESH_TOKEN_DAYS))

# Verify JWT
def verify_jwt(token: str):
    try:
        payload = pyjwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except pyjwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token Expired")
    except pyjwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid Token")

# FastAPI app initialization
app = FastAPI()

# OAuth2 scheme for token authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
async def login(user: userlogin):
    NIC = user.NIC
    passcode = user.passcode

    # Find user in database
    db_user = await collection_user.find_one({"NIC": NIC})

    if not db_user or not verify_password(passcode, db_user["passcode"]):
        raise HTTPException(status_code=401, detail="Invalid NIC or passcode")
    
    # Convert MongoDB ObjectId to string
    db_user = fix_mongo_id(db_user)

    # Generate JWT and refresh token
    access_token = create_jwt({"sub": db_user["NIC"]})
    refresh_token = create_refresh_token({"sub": db_user["NIC"]})

    return JSONResponse(
        content={
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    )
