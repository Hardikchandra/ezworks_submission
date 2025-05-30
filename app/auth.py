from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import User
from app.database import SessionLocal
from datetime import datetime, timedelta
from jose import jwt
import os

SECRET_KEY = "1433ccacdab21652e87e2b577b0339dd569c0156460709ed3be04f25e880eea7"
ALGORITHM = "HS256"

# Dependency to get DB session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# Dependency to ensure the user is an Ops user (mocked for now)
def ops_user(db: Session = Depends(get_db)) -> User:
    # In a real app, you'd get the user ID from a decoded JWT token
    user = db.query(User).filter(User.id == 1).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not user.is_ops:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Not an Ops user"
        )
    return user
