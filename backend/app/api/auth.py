# app/api/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

router = APIRouter()

# JWT settings
import os
SECRET_KEY = os.getenv("SECRET_KEY", "your_super_secret_key_here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

from pydantic import BaseModel

class AuthSchema(BaseModel):
    username: str
    password: str

# -------------------------------
# LOGIN
# -------------------------------
@router.post("/login")
def login(data: AuthSchema, db: Session = Depends(get_db)):
    username = data.username
    password = data.password
    user = db.query(User).filter(User.name == username).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token({"sub": user.name})
    return {"access_token": token, "token_type": "bearer"}

# -------------------------------
# REGISTER (for testing)
# -------------------------------
@router.post("/register")
def register(data: AuthSchema, db: Session = Depends(get_db)):
    username = data.username
    password = data.password
    user_exists = db.query(User).filter(User.name == username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = get_password_hash(password)
    user = User(name=username, password=hashed_password, email=f"{username}@example.com")
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"username": user.name, "status": "registered"}
