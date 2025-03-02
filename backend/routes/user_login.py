from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from ..database import collection_user
from ..models import user
from ..utils.password_hashing import verify_password
from ..utils.jwt_authentication import create_jwt, create_refresh_token, verify_jwt
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
async def login(nic: str, passcode: str):
    db_user = await collection_user.find_one({"NIC": nic})

    if not db_user or not verify_password(passcode, db_user["passcode"]):
        raise HTTPException(status_code=401, detail="Invalid NIC or passcode")

    # generate_JWT_and_refresh_token
    access_token = create_jwt({"sub": db_user["nic"]})
    refresh_token = create_refresh_token({"sub": db_user["nic"]})

    return JSONResponse(
        content={
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    )
    
