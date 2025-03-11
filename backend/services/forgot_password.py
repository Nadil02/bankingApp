import hashlib

import bcrypt
from database import collection_user
from schemas.forgot_password import ForgotPasswordRequestSchema, ForgotPasswordResponseSchema

async def forgot_password_service(request: ForgotPasswordRequestSchema) -> ForgotPasswordResponseSchema:

    nic_bytes = request.nic.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(nic_bytes)
    hashed_nic = sha256_hash.hexdigest()
    print("hashed_nic at forgot password",hashed_nic)
    user_data = await collection_user.find_one({"user_id": request.user_id, "login_nic": hashed_nic})
    if not user_data:
        return ForgotPasswordResponseSchema(status="error", message="User not found.")
    if request.new_password != request.confirm_password:
        return ForgotPasswordResponseSchema(status="error", message="Passwords do not match.")
    
    #hash password
    salt=bcrypt.gensalt()
    hashed_passcode=bcrypt.hashpw(request.new_password.encode('utf-8'),salt)
    
    await collection_user.update_one({"user_id": request.user_id, "login_nic": hashed_nic}, {"$set": {"passcode": hashed_passcode.decode('utf-8')}})

    return ForgotPasswordResponseSchema(status="success", message="Password updated successfully.")