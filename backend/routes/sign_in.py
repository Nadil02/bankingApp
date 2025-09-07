from fastapi import APIRouter, Depends
from schemas.sign_in import SignInRequest, SignInResponse, OtpRequest, OtpResponse, OtpRequest, OtpResendRequest, OtpResendResponse, pictureUploadRequest, pictureUploadResponse, usernameRequest, usernameResponse
from services.sign_in import profilePic_upload_service, sign_in_validation,otp_validation,resend_otp_sign_in, username_load_profilePic_upload_service

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

@router.post("/sign_in_username_load_profilePic_upload", response_model=usernameResponse)
async def username_load_profilePic_upload(username_request: usernameRequest):
    return await username_load_profilePic_upload_service(username_request)

@router.post("/sign_in__profilePic_upload", response_model=pictureUploadResponse)
async def profilePic_upload(profilePic_request: pictureUploadRequest):
    return await profilePic_upload_service(profilePic_request)