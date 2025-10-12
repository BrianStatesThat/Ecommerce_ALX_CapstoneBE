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

### Authentication
- User authentication implemented using **Django’s built-in authentication system**.
- Only authenticated users can perform product CRUD operations.
- (Optional) JWT authentication can be added for additional security.

### API Design
- Built with **Django REST Framework (DRF)**.
- Follows **RESTful principles**:
  - `GET` for retrieving data
  - `POST` for creating resources
  - `PUT`/`PATCH` for updating
  - `DELETE` for deleting
- Proper error handling with **HTTP status codes**:
  - `404` for not found
  - `400` for bad requests

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
