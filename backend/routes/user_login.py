from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import JSONResponse
from schemas.user_login_schemas import UserLogin, RefreshTokenRequest
from utils.auth import verify_token
from services.user_login import login_user, get_user_info_service, refresh_access_token

router = APIRouter()

@router.post("/login")
async def login(user: UserLogin):
    response = await login_user(user)
    return JSONResponse(content=response)

@router.get("/user-info")
async def get_user_info(token_data: dict = Depends(verify_token)):
    user = await get_user_info_service(token_data)
    return user

@router.post("/refresh-token")
async def refresh_token(request: RefreshTokenRequest):
    response = await refresh_access_token(request)
    return JSONResponse(content=response)
