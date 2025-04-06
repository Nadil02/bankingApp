from fastapi import APIRouter, Depends
from schemas.sign_in import SignInRequest, SignInResponse, OtpRequest, OtpResponse, OtpRequest, OtpResendRequest, OtpResendResponse
from services.sign_in import sign_in_validation,otp_validation,resend_otp_sign_in

router = APIRouter()

@router.post("/sign_in", response_model=SignInResponse)
async def sign_in(sign_in_request: SignInRequest):
    return await sign_in_validation(sign_in_request)

@router.post("/sing_in_otp", response_model=OtpResponse)
async def otp(otp_request: OtpRequest):
    return await otp_validation(otp_request)

@router.post("/sign_in_otp_resend", response_model=OtpResendResponse)
async def otp_resend(otp_resend_request: OtpResendRequest):
    return await resend_otp_sign_in(otp_resend_request)