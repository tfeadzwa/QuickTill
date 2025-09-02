# Sales API
from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_sale(item_id: int, quantity: int):
    return {"item_id": item_id, "quantity": quantity, "status": "sale recorded"}
