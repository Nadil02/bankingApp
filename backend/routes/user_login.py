from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from ..database import collection_user
from ..models import user
from ..utils.password_hashing import verify_password
from ..utils.jwt_authentication import create_jwt, create_refresh_token, verify_jwt
from fastapi.responses import JSONResponse
from ..schemas.user_login import userlogin


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#convert_ObjectId_to_string
def fix_mongo_id(document):
    if document and "_id" in document:
        document["_id"] = str(document["_id"])
    return document

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
async def login(user: userlogin):
    NIC = user.NIC
    passcode = user.password

    db_user = await collection_user.find_one({"NIC": NIC})

    if not db_user or not verify_password(passcode, db_user["passcode"]):
        raise HTTPException(status_code=401, detail="Invalid NIC or passcode")
    
    #convert_id_from_object_to_string
    db_user["_id"] = str(db_user["_id"])

    # generate_JWT_and_refresh_token
    access_token = create_jwt({"sub": db_user["NIC"]})
    refresh_token = create_refresh_token({"sub": db_user["NIC"]})

    return JSONResponse(
        content={
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    )
    
