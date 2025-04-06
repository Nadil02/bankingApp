from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("Your Secret Key:", key.decode())  
