from fastapi import APIRouter, Depends
from schemas.forgot_password import ForgotPasswordOtpRequestResponseSchema, ForgotPasswordOtpRequestSchema, ForgotPasswordOtpResendRequestSchema, ForgotPasswordOtpResendResponseSchema, ForgotPasswordRequestSchema, ForgotPasswordResponseSchema
from services.forgot_password import forgot_password_otp_request_service, forgot_password_otp_resend_request_service, forgot_password_service

router = APIRouter()

@router.post("/forgot_password", response_model=ForgotPasswordResponseSchema)
async def forgot_password(request: ForgotPasswordRequestSchema = Depends()): #depends use to validate format
    return await forgot_password_service(request)

@router.post("/forgot_password_otp_request", response_model=ForgotPasswordOtpRequestResponseSchema)
async def forgot_password_otp_request(request: ForgotPasswordOtpRequestSchema = Depends()):
    return await forgot_password_otp_request_service(request)

@router.post("/forgot_password_otp_resend_request", response_model=ForgotPasswordOtpResendResponseSchema)
async def forgot_password_otp_resend_request(request: ForgotPasswordOtpResendRequestSchema = Depends()):
    return await forgot_password_otp_resend_request_service(request)