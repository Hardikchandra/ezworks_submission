from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    is_ops = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)

class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
