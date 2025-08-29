# Entry point for POS Invoicing App
from fastapi import FastAPI
from app.api import auth, products, sales, invoices

app = FastAPI(title="POS & Invoicing API")

# Register routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(sales.router, prefix="/sales", tags=["Sales"])
app.include_router(invoices.router, prefix="/invoices", tags=["Invoices"])

@app.get("/")
def root():
    return {"message": "POS & Invoicing System API running 🚀"}
