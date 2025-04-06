from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv
from models import user

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY").encode()
cipher_suite = Fernet(SECRET_KEY)

def encrypt(data: str) -> str:
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt(data: str) -> str:
    return cipher_suite.decrypt(data.encode()).decode()

def decrypt_user_data(user: user) -> user:
    user.first_name = decrypt(user.first_name)
    user.last_name = decrypt(user.last_name)
    user.nic = decrypt(user.nic)
    user.phone_number = decrypt(user.phone_number)
    user.passcode=user.passcode
    user.user_id=user.user_id
    user.notification_status=user.notification_status
    return user