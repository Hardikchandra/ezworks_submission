from fastapi import APIRouter, Depends
from app.auth import create_access_token, hash_password, verify_password
from app.models import User, File
from app.database import SessionLocal
from app.utils import generate_secure_url
from jose import jwt
from app.schemas import UserCreate
from sqlalchemy.orm import Session
from app.database import get_db

    # your logic here

router = APIRouter()

@router.post("/signup")
def signup(data: UserCreate, db: Session = Depends(get_db)):
    hashed = hash_password(data.password)
    user = User(email=data.email, password=hashed)
    db.add(user)
    db.commit()
    url = f"/verify-email/{user.id}"  # mock verification
    return {"url": url}

@router.get("/verify-email/{user_id}")
def verify(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_verified = True
    db.commit()
    db.refresh(user)
    return {"message": "Email verified", "user_id": user.id, "verified": user.is_verified}


@router.get("/download-file/{token}")
def download_file(token: str, db=Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        file_id = payload.get("file_id")
        if not file_id:
            raise HTTPException(status_code=400, detail="Invalid token")
        
        file = db.query(File).filter(File.id == file_id).first()
        if not file:
            raise HTTPException(status_code=404, detail="File not found")
        
    
        return {"message": "File found", "filename": file.filename}

    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid or expired token")

@router.get("/client/generate-token/{file_id}")
def generate_file_token(file_id: int):
    token = create_access_token({"file_id": file_id})
    return {"token": token}
