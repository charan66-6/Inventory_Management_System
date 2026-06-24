# 📦 Inventory Management System

## 📌 Project Overview

The Inventory Management System is a full-stack application built using **Python**, **FastAPI**, and **Streamlit**. The project helps manage product inventory efficiently by allowing users to add, update, delete, search, and monitor products in stock.

The application automatically tracks product quantities and provides stock alerts when inventory levels become low.

---

## 🚀 Technologies Used

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

### Frontend

* Streamlit
* Requests Library

---

## ✨ Features

### 1. View Products

* Display all available products.
* Shows Product ID, Product Name, Price, and Quantity.
* Displays stock status:

  * 🟢 In Stock
  * 🟡 Limited Stock
  * 🔴 Low Stock

### 2. Add Product

* Add new products to inventory.
* Product ID is generated automatically.
* New products are stored instantly.

### 3. Update Product

* Modify product information.
* Update:

  * Product Name
  * Price
  * Quantity

### 4. Delete Product

* Remove products from inventory using Product ID.

### 5. Search Product

* Search products by name.
* Matching products are displayed immediately.

### 6. Quantity Management

* Increase quantity using ➕ button.
* Decrease quantity using ➖ button.
* Inventory updates dynamically.

### 7. Low Stock Alert

* Automatically detects products with quantity less than 5.
* Displays low-stock products separately.

### 8. Inventory Summary

Shows:

* Total Products
* Total Stock Quantity
* Total Inventory Value

---

## 📂 Project Structure

```text
Inventory_Management/
│
├── backend.py          # FastAPI Backend
├── app.py              # Streamlit Frontend
├── requirements.txt
├── README.md
└── venv/
```

---

## 🔧 API Endpoints

### Get All Products

```http
GET /products
```

Returns all products in inventory.

---

### Add Product

```http
POST /products
```

Adds a new product with automatically generated Product ID.

---

### Update Product

```http
PUT /products/{product_id}
```

Updates product details.

---

### Delete Product

```http
DELETE /products/{product_id}
```

Deletes a product.

---

### Update Quantity

```http
PATCH /products/{product_id}/quantity
```

Increases or decreases product quantity dynamically.

---

### Low Stock Products

```http
GET /low-stock
```

Returns products whose quantity is less than 5.

---

### Inventory Summary

```http
GET /summary
```

Returns:

```json
{
  "total_products": 6,
  "total_quantity": 42,
  "inventory_value": 896400
}
```

---

## ▶️ How to Run the Project

### Step 1: Create Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install fastapi uvicorn streamlit requests
```

---

## ▶️ Run Backend

```bash
uvicorn backend:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Frontend

Open a new terminal and run:

```bash
streamlit run app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

## 📊 Stock Status Logic

| Quantity | Status           |
| -------- | ---------------- |
| >= 10    | 🟢 In Stock      |
| 5 - 9    | 🟡 Limited Stock |
| < 5      | 🔴 Low Stock     |

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Building REST APIs using FastAPI
* Using Pydantic for data validation
* Connecting FastAPI with Streamlit
* CRUD Operations (Create, Read, Update, Delete)
* Dynamic Quantity Management
* API Integration using Requests
* Frontend Development with Streamlit
* Inventory Management Concepts

---

## 📌 Future Improvements

* Database Integration (MySQL/PostgreSQL)
* User Authentication
* Product Categories
* Sales Tracking
* Purchase Orders
* Export Inventory Reports
* Dashboard Analytics
* Cloud Deployment

---

## 👨‍💻 Author

**Vidhya Charan**

Python Developer | FastAPI | Streamlit | Backend Development
