# from passlib.context import CryptContext
from pwdlib import PasswordHash

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
password_hash = PasswordHash.recommended()

def hash(password: str):
    return password_hash.hash(password)


def verify(plain_password, hased_password):
    return password_hash.verify(plain_password,hased_password)