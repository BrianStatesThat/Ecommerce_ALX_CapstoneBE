from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Product, Category

class ProductViewTest(APITestCase):
    def setUp(self):
        # Create test user and category
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.category = Category.objects.create(name="Clothing")

        # Obtain JWT token
        token_response = self.client.post("/api/token/", {
            "username": "testuser",
            "password": "testpass"
        })
        self.assertEqual(token_response.status_code, 200)
        self.token = token_response.data["access"]

    def test_create_product_authenticated(self):
        # Set Authorization header with JWT token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        data = {
            "name": "T-Shirt",
            "description": "Cotton",
            "price": 19.99,
            "category": self.category.id,
            "stock_quantity": 100,
            "image_url": "http://example.com/tshirt.jpg"
        }
        response = self.client.post("/api/products/", data)
        self.assertEqual(response.status_code, 201)

    def test_create_product_unauthenticated(self):
        # Ensure no credentials are set
        self.client.credentials()

        data = {
            "name": "Unauthorized Shirt",
            "description": "Should fail",
            "price": 10.00,
            "category": self.category.id,
            "stock_quantity": 50,
            "image_url": "http://example.com/fail.jpg"
        }
        response = self.client.post("/api/products/", data)
        self.assertEqual(response.status_code, 401)