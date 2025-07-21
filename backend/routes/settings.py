from fastapi import APIRouter, HTTPException, Depends
from schemas.settings import OtpRequestEditTphone, OtpResendRequestEditTphone, OtpResponseEditTphone, getUserNotificationStatus,updateUserNotificationStatus, UserEditProfile, EditProfileResponse
from services.settings import get_user_notification_status, otp_validation_Tphone_edit, resend_otp_eidt_Tphone, update_user_notification_status, load_edit_profile, update_new_details
from schemas.sign_in import SignInRequest, OtpRequest, SignInResponse
from fastapi.responses import JSONResponse

from utils.auth import verify_token

router = APIRouter(
    prefix="/settings",
    tags=["settings"],
    dependencies=[Depends(verify_token)]
)

@router.get("/", response_model=getUserNotificationStatus)
async def get_user_info(user_id: int):
    # Get the user's notification status
    user_status = await get_user_notification_status(user_id)
    if user_status is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_status

@router.post("/", response_model=updateUserNotificationStatus)
async def update_user_info(user_id: int, status: bool):
    # Update the user's notification status
    updated_status = await update_user_notification_status(user_id, status)
    if updated_status is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_status

# route for getting the user's profile details
@router.get("/edit_profile", response_model=UserEditProfile)
async def get_edit_profile(user_id: int):
    return await load_edit_profile(user_id)

# route for updating the user's profile details without changing the phone number
@router.post("/edit_profile", response_model=EditProfileResponse)
async def update_edit_profile(request: UserEditProfile):    
    return await update_new_details(request)

@router.post("/edit_phone_number_otp", response_model=OtpResponseEditTphone)
async def otp(otp_request: OtpRequestEditTphone):
    return await otp_validation_Tphone_edit(otp_request)

@router.post("/edit_phone_otp_resend", response_model=OtpResponseEditTphone)
async def otp_resend(otp_resend_request: OtpResendRequestEditTphone):
    return await resend_otp_eidt_Tphone(otp_resend_request)