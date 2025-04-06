# services/auth_service.py
import logging
from fastapi import HTTPException
from starlette.responses import JSONResponse
from utils.auth import create_jwt, create_refresh_token, verify_jwt, verify_token
from database import collection_user as user_collection
from utils.encrypt_and_decrypt import decrypt,encrypt
from argon2 import PasswordHasher,exceptions
import hashlib
import bcrypt
ph = PasswordHasher()


async def fix_mongo_id(document):
    if document and "_id" in document:
        document["_id"] = str(document["_id"])  # Convert ObjectId to string
    return document

async def login_user(user):
    logging.info(f"Login request received for NIC: {user.nic}")

    nic_bytes = user.nic.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(nic_bytes)
    hashed_nic = sha256_hash.hexdigest()
    
    print("hashed_nic at login",hashed_nic)
    db_user = await user_collection.find_one({"login_nic": hashed_nic})
    if not db_user:
        logging.warning(f"User with NIC {user.nic} not found in database.")
        raise HTTPException(status_code=404, detail="User not found")

    # if not ph.verify(user.passcode,db_user.get("passcode")):
    #     logging.warning(f"Invalid passcode for NIC {user.nic}")
    #     raise HTTPException(status_code=401, detail="Invalid NIC or passcode")
    
    print("passcode",db_user.get("passcode"))

    if not bcrypt.checkpw(user.passcode.encode('utf-8'), db_user.get("passcode").encode('utf-8')):
        logging.warning(f"Invalid passcode for NIC {user.nic}")
        raise HTTPException(status_code=401, detail="Invalid NIC or passcode")
    else:
        print("password matched")

    db_user = await fix_mongo_id(db_user)

    access_token = create_jwt({"sub": db_user["NIC"]})
    refresh_token = create_refresh_token({"sub": db_user["NIC"]})

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer", "user_id": db_user["user_id"]}

async def get_user_info_service(token_data):
    user = await user_collection.find_one({"NIC": token_data["sub"]})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await fix_mongo_id(user)

async def refresh_access_token(request):
    payload = verify_jwt(request.refresh_token)
    if "error" in payload:
        raise HTTPException(status_code=401, detail=payload["error"])
    
    new_access_token = create_jwt({"sub": payload["sub"]})
    return {"access_token": new_access_token, "token_type": "bearer"}
