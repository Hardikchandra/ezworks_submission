import uuid
from fastapi.responses import FileResponse
from jose import jwt

def generate_secure_url(file_id: int, user_id: int):
    token = jwt.encode({"file_id": file_id, "user_id": user_id}, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return f"/download-file/{token}"
