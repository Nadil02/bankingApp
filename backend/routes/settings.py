from fastapi import APIRouter, HTTPException, Depends
from schemas.settings import UserNotificationStatus, UserEditProfile
from services.settings import get_user_notification_status, update_user_notification_status, load_edit_profile, update_new_details, send_sms
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/settings",
    tags=["settings"],
)

@router.get("/", response_model=UserNotificationStatus)
async def get_user_info(user_id: int):
    # Get the user's notification status
    user_status = await get_user_notification_status(user_id)
    if user_status is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_status

@router.post("/", response_model=UserNotificationStatus)
async def update_user_info(user_id: int, status: bool):
    # Update the user's notification status
    updated_status = await update_user_notification_status(user_id, status)
    if updated_status is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_status

# route to edit the user's profile
@router.get("/edit_profile", response_model=UserEditProfile)
async def get_edit_profile(user_id: int):
    return await load_edit_profile(user_id)

# route to update the user's profile
@router.post("/edit_profile", response_model=UserEditProfile)
async def update_edit_profile(request: UserEditProfile):
    return await update_new_details(request)

# send otp route
@router.get("/send_otp")
async def send_otp(phone_number: str):
    return await send_sms(phone_number, "Hello from Notify.lk!")
