import bcrypt
from database import collection_user
from schemas.change_password import ChangePasswordRequestSchema, ChangePasswordResponseSchema

async def change_password_service(request: ChangePasswordRequestSchema) -> ChangePasswordResponseSchema:
    user_data = await collection_user.find_one({"user_id": request.user_id})

    if not user_data:
        return ChangePasswordResponseSchema(status="error", message="User not found.")

    # Check old password
    if not bcrypt.checkpw(request.old_password.encode('utf-8'), user_data["passcode"].encode('utf-8')):
        return ChangePasswordResponseSchema(status="error", message="Incorrect old password.")

    if request.new_password != request.confirm_password:
        return ChangePasswordResponseSchema(status="error", message="New passwords do not match.")

    # Hash new password
    salt = bcrypt.gensalt()
    hashed_new_password = bcrypt.hashpw(request.new_password.encode('utf-8'), salt).decode('utf-8')

    # Update user password
    await collection_user.update_one({"user_id": request.user_id}, {"$set": {"passcode": hashed_new_password}})

    return ChangePasswordResponseSchema(status="success", message="Password updated successfully.")
