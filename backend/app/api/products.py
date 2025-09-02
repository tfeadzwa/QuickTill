# app/api/products.py
from fastapi import APIRouter, Depends
from app.api.dependencies import get_current_user
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.product import Product

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", dependencies=[Depends(get_current_user)])
def list_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products
