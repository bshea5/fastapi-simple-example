
from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
  def encrypt(password: str):
    return pwd_cxt.hash(password)

  def verify(attempt, encrypted_password):
    return pwd_cxt.verify(attempt, encrypted_password)