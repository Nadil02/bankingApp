from fastapi import APIRouter, Depends
from schemas.forgot_password import ForgotPasswordRequestSchema, ForgotPasswordResponseSchema
from services.forgot_password import forgot_password_service

router = APIRouter()

@router.post("/forgot_password", response_model=ForgotPasswordResponseSchema)
async def forgot_password(request: ForgotPasswordRequestSchema = Depends()): #depends use to validate format
    return await forgot_password_service(request)