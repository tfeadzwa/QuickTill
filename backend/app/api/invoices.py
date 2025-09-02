# Invoices API
from fastapi import APIRouter

router = APIRouter()

@router.get("/{invoice_id}")
async def get_invoice(invoice_id: int):
    return {"invoice_id": invoice_id, "status": "fetched"}
