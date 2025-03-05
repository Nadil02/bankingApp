from database import collection_user
from schemas.forgot_password import ForgotPasswordRequestSchema, ForgotPasswordResponseSchema

async def forgot_password_service(request: ForgotPasswordRequestSchema) -> ForgotPasswordResponseSchema:
    user_data = await collection_user.find_one({"user_id": request.user_id, "nic": request.nic})
    if not user_data:
        return ForgotPasswordResponseSchema(status="error", message="User not found.")
    if request.new_password != request.confirm_password:
        return ForgotPasswordResponseSchema(status="error", message="Passwords do not match.")
    
    # need to hash password
    
    await collection_user.update_one({"user_id": request.user_id, "nic": request.nic}, {"$set": {"password": request.new_password}})

    return ForgotPasswordResponseSchema(status="success", message="Password updated successfully.")