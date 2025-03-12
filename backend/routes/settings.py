from fastapi import APIRouter, HTTPException, Depends
from schemas.settings import UserNotificationStatus
from services.settings import get_user_notification_status, update_user_notification_status
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/settings", response_model=UserNotificationStatus)
async def get_user_info(user_id: int):
    # Get the user's notification status
    user_status = await get_user_notification_status(user_id)
    if user_status is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_status

@router.post("/settings", response_model=UserNotificationStatus)
async def update_user_info(user_id: int, status: bool):
    # Update the user's notification status
    updated_status = await update_user_notification_status(user_id, status)
    if updated_status is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_status
