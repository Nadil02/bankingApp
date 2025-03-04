from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import JSONResponse
from models import UserLogin, RefreshTokenRequest
from auth import create_jwt, create_refresh_token, verify_jwt, verify_token
from database import user_collection
import logging

router = APIRouter()

async def fix_mongo_id(document):
    if document and "_id" in document:
        document["_id"] = str(document["_id"])  # Convert ObjectId to string
    return document

@router.post("/login")
async def login(user: UserLogin):
    logging.info(f"Login request received for NIC: {user.nic}")

    # Fix field name issue (use "nic" instead of "NIC")
    db_user = await user_collection.find_one({"nic": user.nic})  # Ensure case matches MongoDB field

    if not db_user:
        logging.warning(f"User with NIC {user.nic} not found in database.")
        raise HTTPException(status_code=404, detail="User not found")

    if user.passcode != db_user.get("passcode"):
        logging.warning(f"Invalid passcode for NIC {user.nic}")
        raise HTTPException(status_code=401, detail="Invalid NIC or passcode")

    db_user = await fix_mongo_id(db_user)

    access_token = create_jwt({"sub": db_user["nic"]})
    refresh_token = create_refresh_token({"sub": db_user["nic"]})

    return JSONResponse(
        content={"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}
    )

@router.get("/user-info")
async def get_user_info(token_data: dict = Depends(verify_token)):
    user = await user_collection.find_one({"nic": token_data["sub"]})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user = await fix_mongo_id(user)
    return user

@router.post("/refresh-token")
async def refresh_token(request: RefreshTokenRequest):
    payload = verify_jwt(request.refresh_token)

    if "error" in payload:
        raise HTTPException(status_code=401, detail=payload["error"])

    new_access_token = create_jwt({"sub": payload["sub"]})

    return JSONResponse(content={"access_token": new_access_token, "token_type": "bearer"})
