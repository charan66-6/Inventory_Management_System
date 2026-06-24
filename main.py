from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Inventory Management System")


# ======================
# Product Model
# ======================

class Product(BaseModel):
    name: str
    price: float
    quantity: int


# ======================
# Initial Inventory
# ======================

inventory = {
    1: {
        "name": "Laptop",
        "price": 65000,
        "quantity": 10
    },
    2: {
        "name": "Mobile Phone",
        "price": 25000,
        "quantity": 4
    },
    3: {
        "name": "Keyboard",
        "price": 1200,
        "quantity": 15
    },
    4: {
        "name": "Mouse",
        "price": 800,
        "quantity": 3
    },
    5: {
        "name": "Monitor",
        "price": 12000,
        "quantity": 8
    },
    6: {
        "name": "Printer",
        "price": 15000,
        "quantity": 2
    }
}


# ======================
# Generate Product ID
# ======================

def generate_product_id():
    if inventory:
        return max(inventory.keys()) + 1
    return 1


# ======================
# Home
# ======================

@app.get("/")
def home():
    return {
        "message": "Inventory Management API Running"
    }


# ======================
# View All Products
# ======================

@app.get("/products")
def get_products():
    return inventory


# ======================
# View Single Product
# ======================

@app.get("/products/{product_id}")
def get_product(product_id: int):

    if product_id not in inventory:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    return inventory[product_id]


# ======================
# Add Product
# ======================

@app.post("/products")
def add_product(product: Product):

    new_id = generate_product_id()

    inventory[new_id] = product.model_dump()

    return {
        "message": "Product Added Successfully",
        "product_id": new_id,
        "product": inventory[new_id]
    }


# ======================
# Update Product
# ======================

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: Product
):

    if product_id not in inventory:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    inventory[product_id] = product.model_dump()

    return {
        "message": "Product Updated Successfully",
        "product": inventory[product_id]
    }


# ======================
# Increase / Decrease Quantity
# ======================

@app.patch("/products/{product_id}/quantity")
def update_quantity(
    product_id: int,
    change: int
):

    if product_id not in inventory:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    inventory[product_id]["quantity"] += change

    # Prevent negative quantity
    if inventory[product_id]["quantity"] < 0:
        inventory[product_id]["quantity"] = 0

    return {
        "message": "Quantity Updated Successfully",
        "product_id": product_id,
        "new_quantity": inventory[product_id]["quantity"]
    }


# ======================
# Delete Product
# ======================

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    if product_id not in inventory:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    deleted_product = inventory.pop(product_id)

    return {
        "message": "Product Deleted Successfully",
        "deleted_product": deleted_product
    }


# ======================
# Low Stock Products
# ======================

@app.get("/low-stock")
def low_stock():

    low_items = {}

    for product_id, item in inventory.items():

        if item["quantity"] < 5:

            low_items[product_id] = {
                **item,
                "alert": "Stock is very low"
            }

    return low_items


# ======================
# Inventory Summary
# ======================

@app.get("/summary")
def summary():

    total_products = len(inventory)

    total_quantity = sum(
        item["quantity"]
        for item in inventory.values()
    )

    total_value = sum(
        item["price"] * item["quantity"]
        for item in inventory.values()
    )

    return {
        "total_products": total_products,
        "total_quantity": total_quantity,
        "inventory_value": total_value
    }