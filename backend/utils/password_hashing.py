from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

#hash_password_before_storing_in_db
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

#verify_input_password_with_hashed_password_from_db
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)