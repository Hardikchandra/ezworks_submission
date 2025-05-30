from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import os
from app.database import get_db
from app.auth import ops_user
from app.models import File as FileModel

router = APIRouter()

@router.post("/upload")
def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(ops_user)
):
    # 1. Validate file type (optional)
    allowed_extensions = (".docx", ".pptx", ".xlsx")
    if not file.filename.endswith(allowed_extensions):
        raise HTTPException(status_code=400, detail="Invalid file format")

    # 2. Ensure files/ directory exists
    os.makedirs("files", exist_ok=True)

    # 3. Save file to disk
    file_path = f"files/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # 4. Save metadata in database
    new_file = FileModel(filename=file.filename, owner_id=current_user.id)
    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return {"message": "File uploaded successfully", "file_id": new_file.id}
