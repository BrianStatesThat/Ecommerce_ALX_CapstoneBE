from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Product, Category

class ProductViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.category = Category.objects.create(name="Clothing")
        self.client.login(username="testuser", password="testpass")

    def test_create_product_authenticated(self):
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
        self.client.logout()
        response = self.client.post("/api/products/", {})
        self.assertEqual(response.status_code, 401)