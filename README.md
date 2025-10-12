# E-commerce Product API

## Project Overview
This project is a **Backend E-commerce Product API** built with **Django** and **Django REST Framework (DRF)**.  
The API serves as the backend for managing products on an e-commerce platform, allowing authenticated users to **create, update, delete, and view products**.  
It simulates real-world backend development responsibilities, focusing on **product management, user authentication, and product search functionality**.

---

## Features

### Product Management (CRUD)
- Create, Read, Update, and Delete products.
- Product attributes:
  - Name
  - Description
  - Price
  - Category
  - Stock Quantity
  - Image URL
  - Created Date
- Validation for required fields: **Name, Price, Stock Quantity**.
- (Optional/Future) Stock Quantity automatically decreases when an order is placed.

### User Management (CRUD)
- Manage users who can manage products.
- User attributes:
  - Unique Username
  - Email
  - Password
- Only authenticated users can manage products.

### Product Search
- Search products by **Name** or **Category**.
- Supports **partial matches** for flexible search results.
- Includes **pagination** for handling large datasets.

### Product View
- Retrieve a list of products or individual product details by **Product ID**.
- Optional filters:
  - Category
  - Price Range
  - Stock Availability
- Product details include all relevant information: Name, Description, Price, Category, Stock Quantity, Image URL.

---

## Technical Specifications

### Database
- Uses **Django ORM** to interact with the database.
- Models defined for:
  - **Products**
  - **Users**
- Products are associated with categories (e.g., Electronics, Clothing).

# E-commerce Product API Endpoints

This API is built using Django and Django REST Framework. It supports product and user management, authentication, search, filtering, and documentation.

---

##  Authentication

- `POST /api/token/`  
  Obtain JWT access and refresh tokens.

- `POST /api/token/refresh/`  
  Refresh access token using a valid refresh token.

---

## Users

- `GET /api/users/`  
  List all users.

- `POST /api/users/`  
  Register a new user.

- `GET /api/users/{id}/`  
  Retrieve user details.

- `PUT /api/users/{id}/`  
  Update user information.

- `DELETE /api/users/{id}/`  
  Delete a user.

---

##  Products (`mystore` app)

- `GET /api/products/`  
  List all products (supports pagination, search, and filtering).

- `POST /api/products/`  
  Create a new product (requires authentication).

- `GET /api/products/{id}/`  
  Retrieve details for a specific product.

- `PUT /api/products/{id}/`  
  Update a product (requires authentication).

- `DELETE /api/products/{id}/`  
  Delete a product (requires authentication).

---

##  Search & Filtering

- `GET /api/products/?search=keyword`  
  Search products by name or category (partial matches supported).

- `GET /api/products/?category=1&min_price=50&max_price=200&in_stock=true`  
  Filter products by category, price range, and stock availability.

---

##  Categories

- `GET /api/categories/`  
  List all categories.

- `POST /api/categories/`  
  Create a new category (requires authentication).

- `GET /api/categories/{id}/`  
  Retrieve category details.

- `PUT /api/categories/{id}/`  
  Update a category.

- `DELETE /api/categories/{id}/`  
  Delete a category.

---

### Pagination & Filtering
- Pagination added to product listings and search results.
- Filtering options include:
  - Category
  - Price Range
  - Stock Availability
## Getting Started

### Prerequisites
- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL or SQLite (for development)
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ecommerce-product-api
