from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.responses import JSONResponse
import jwt as pyjwt
import os
from datetime import datetime, timedelta
from pydantic import BaseModel
import motor.motor_asyncio
from dotenv import load_dotenv
import logging
#from database import collection_user # Now database.py should be found

import motor.motor_asyncio
import os
from dotenv import load_dotenv

# load environment variables from the .env file
load_dotenv()

# MongoDB URI from .env file
MONGO_URI = os.getenv("MONGO_URI")

# create a client instance for MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

# database
db = client["project"] 

collection_user = db["user"]


app = FastAPI()

# Secret key and algorithm for signing the JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class userlogin(BaseModel):
    NIC: str
    passcode: str

def fix_mongo_id(document):
    if document and "_id" in document:
        document["_id"] = str(document["_id"])  # Convert ObjectId to string
    return document

def create_jwt(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})

    return pyjwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict, expires_delta: timedelta = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})

    return pyjwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.get("/")
async def read_root(NIC: str = Query(..., description="National Identity Card number")):
    db_user = await collection_user.find_one({"NIC": NIC})
    if db_user:
        return fix_mongo_id(db_user)
    return {"error": "User not found"}

@app.post("/loginn_C")
async def login(user: userlogin):
    NIC = user.NIC
    passcode = user.passcode

    # Log the incoming NIC and passcode for debugging
    logger.debug(f"Login attempt with NIC: {NIC} and passcode: {passcode}")

    try:
        # Query the database for the user with the provided NIC
        db_user = await collection_user.find_one({"NIC": NIC})

        if not db_user:
            logger.error(f"User with NIC {NIC} not found in database.")
            raise HTTPException(status_code=404, detail="User not found")

        # Check if the passcode matches (This example does not use hash comparison, but you can modify it to use hashed passwords)
        if passcode != db_user.get("passcode"):
            logger.error(f"Invalid passcode for NIC {NIC}.")
            raise HTTPException(status_code=401, detail="Invalid NIC or passcode")

        # Fix _id if present
        db_user = fix_mongo_id(db_user)

        # Generate JWT and refresh tokens
        access_token = create_jwt({"sub": db_user["NIC"]})
        refresh_token = create_refresh_token({"sub": db_user["NIC"]})

        # Return tokens in the response
        return JSONResponse(
            content={
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer"
            }
        )

    except Exception as e:
        logger.error(f"An error occurred during login: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
