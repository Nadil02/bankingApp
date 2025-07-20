import asyncio
from utils.encrypt_and_decrypt import decrypt, encrypt, decrypt_user_data
from argon2 import PasswordHasher
import hashlib
import bcrypt
import base64
from database import collection_user,collection_OTP

# User ID to update
USER_ID = 1

# Image file to upload
IMAGE_PATH = "D:/SEProject/backend/backend/download.jpeg"  # e.g., "images/profile.png"

# ---------------------------
# Read and encrypt image
# ---------------------------

def read_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode('utf-8')
    return encoded

def encrypt_base64_image(base64_str):
    return encrypt(base64_str)

# ---------------------------
# Update MongoDB
# ---------------------------

async def update_user_image():

    # Convert image
    base64_img = read_image_as_base64(IMAGE_PATH)
    encrypted_img = encrypt_base64_image(base64_img)

    # Update MongoDB
    result = await collection_user.update_one(
        {"user_id": USER_ID},
        {"$set": {"user_image": encrypted_img}}
    )

    if result.modified_count:
        print("✅ User image encrypted and updated successfully.")
    else:
        print("⚠️ No document was updated. Check if the user ID is correct.")

# ---------------------------
# Run the script
# ---------------------------

if __name__ == "__main__":
    asyncio.run(update_user_image())