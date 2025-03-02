from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from database import users_collection
from models import User
from security import verify_password
from auth import create_jwt, create_refresh_token, verify_jwt

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
def login(nic: str, passcode: str):
    db_user = users_collection.find_one({"nic": nic})

    if not db_user or not verify_password(passcode, db_user["passcode"]):
        raise HTTPException(status_code=401, detail="Invalid NIC or passcode")

    # generate_JWT_and_refresh_token
    access_token = create_jwt({"sub": db_user["nic"]})
    refresh_token = create_refresh_token({"sub": db_user["nic"]})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }
