from fastapi import APIRouter, HTTPException, Depends
from schemas.change_password import ChangePasswordRequestSchema, ChangePasswordResponseSchema
from services.change_password import change_password_service

router = APIRouter()

@router.post("/change-password", response_model=ChangePasswordResponseSchema)
async def change_password(request: ChangePasswordRequestSchema):
    response = await change_password_service(request)
    if response.status == "error":
        raise HTTPException(status_code=400, detail=response.message)
    return response
