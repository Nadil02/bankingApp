import base64
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY").encode()
cipher_suite = Fernet(SECRET_KEY)

def encrypt(data: str) -> str:
    return cipher_suite.encrypt(data.encode()).decode()

def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

# Example usage
image_path = '../download.png'  # change this to your image path
base64_string = convert_image_to_base64(image_path)


print("image to base64 : " + base64_string)  # This will print the base64 string

encrypted_string = encrypt(base64_string)
print("encrypted string : " + encrypted_string)  # This will print the encrypted string
