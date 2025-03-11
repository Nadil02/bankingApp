from fastapi import APIRouter, Depends
from schemas import SignInRequest, SignInResponse, OtpRequest, OtpResponse, OtpRequest
from services.sign_in import sign_in_validation,otp_validation

router = APIRouter()

@router.post("/sign_in", response_model=SignInResponse)
async def sign_in(sign_in_request: SignInRequest):
    return await sign_in_validation(sign_in_request)

@router.post("/otp", response_model=OtpResponse)
async def otp(otp_request: OtpRequest):
    return await otp_validation(otp_request)