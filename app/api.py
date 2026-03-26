from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator, field_validator
from app.db import list_products, get_product_by_id as db_get_product_by_id, create_product as db_create_product, update_stock as db_update_stock, delete_product as db_delete_product
from psycopg.errors import UniqueViolation


app = FastAPI()

COLUMNS = ["id", "sku", "name", "price", "stock", "is_active", "created_at"]

"""@app.get("/products")
def get_products():
    products = list_products()
    return products"""
    
class NewProduct(BaseModel):
    sku: str = Field(..., pattern="^SKU\d{3}$")
    name: str = Field("Any", min_length=3)
    price: float = Field(..., ge=0.1)
    stock: int = Field(..., gt=0)
    
class NewStock(BaseModel):
    stock: int = Field(..., ge=0)
                
    
@app.get("/")
def main():
    return {"message": "API Products running"}

#GET /products
@app.get("/products")
def get_products():
    rows = list_products()
    return [dict(zip(COLUMNS, row)) for row in rows]

#GET /products/{id}
@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    product = db_get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return dict(zip(COLUMNS, product))

#POST /products
@app.post("/products", status_code=201)
def create_product(np: NewProduct):

    try:
        new_product = db_create_product(np.sku, np.name, np.price, np.stock)
    except UniqueViolation:
        raise HTTPException(status_code=409, detail="SKU já existente. Pfv introduza um novo SKU único para criar novo produto.")
    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno ao criar produto.")
        
    return {"id": new_product, "sku": np.sku, "name": np.name, "price": np.price, "stock": np.stock}

#PATCH /products/{id}/stock
@app.patch("/products/{product_id}/stock")
def update_stock(product_id: int, ns: NewStock):
    new_stock = db_update_stock(product_id, ns.stock)

    if new_stock is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return {"id": new_stock, "stock": ns.stock , "message": "Stock atualizado."}

#DELETE /products/{id}
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    deleted_product = db_delete_product(product_id)
    
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return {"id": deleted_product, "message": "Produto removido."}