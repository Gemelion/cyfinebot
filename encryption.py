
from cryptography.fernet import Fernet
import os

KEY = os.getenv("SECRET_KEY", Fernet.generate_key())
cipher = Fernet(KEY)

def encrypt(text: str) -> str:
    return cipher.encrypt(text.encode()).decode()

def decrypt(token: str) -> str:
    return cipher.decrypt(token.encode()).decode()
