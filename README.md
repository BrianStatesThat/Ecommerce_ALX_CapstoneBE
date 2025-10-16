# E-commerce APP

## Project Overview
This project is a **Backend E-commerce Product API** built with **Django** and **Django REST Framework (DRF)**.  
The API serves as the backend for managing products on an e-commerce platform, allowing authenticated users to **create, update, delete, and view products**.  
It simulates real-world backend development responsibilities, focusing on **product management, user authentication, product reviews, and product search functionality**.

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

### User Management (CRUD & Auth)
- Register and authenticate users.
- User attributes:
  - Unique Username
  - Email
  - Password
- Only authenticated users can manage products and reviews.

### Product Search & Filtering
- Search products by **Name** or **Category**.
- Supports **partial matches** for flexible search results.
- Includes **pagination** for handling large datasets.
- Filter products by category, price range, and stock availability.

### Product View
- Retrieve a list of products or individual product details by **Product ID**.
- Optional filters:
  - Category
  - Price Range
  - Stock Availability
- Product details include all relevant information: Name, Description, Price, Category, Stock Quantity, Image URL.

### Categories
- Create, list, update, and delete categories.
- Products are associated with categories (e.g., Electronics, Clothing).

### Reviews
- Add and view reviews for products.
- Review attributes:
  - Rating
  - Comment
  - User
  - Created Date

---

## Technical Specifications

- Uses **Django ORM** to interact with the database.
- Models defined for:
  - **Products**
  - **Categories**
  - **Reviews**
  - **Users** (Django built-in)
- JWT authentication via **djangorestframework-simplejwt**.

---

## API Endpoints

### Authentication

- `POST /api/register/`  
  Register a new user.

- `POST /api/login/`  
  Obtain JWT access and refresh tokens.

- `POST /api/token/refresh/`  
  Refresh access token using a valid refresh token.

---

### Users

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

### Products (`mystore` app)

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

### Reviews

- `GET /api/reviews/?product=<product_id>`  
  List all reviews for a specific product.

- `POST /api/reviews/`  
  Add a new review to a product (requires authentication).

---

### Categories

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

### Search & Filtering

- `GET /api/products/?search=keyword`  
  Search products by name or category (partial matches supported).

- `GET /api/products/?category=1&min_price=50&max_price=200&in_stock=true`  
  Filter products by category, price range, and stock availability.

---

### Pagination & Filtering
- Pagination added to product listings and search results.
- Filtering options include:
  - Category
  - Price Range
  - Stock Availability

---

## Getting Started

### Prerequisites
- Python 3.10+
- Django 4.x or 5.x
- Django REST Framework
- djangorestframework-simplejwt
- PostgreSQL or SQLite (for development)
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ecommerce-product-api
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Make migrations and migrate:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Usage

- Use the provided endpoints to register, login, and manage products, categories, and reviews.
- Authenticate using JWT tokens for protected endpoints.

---

## License

MIT License
