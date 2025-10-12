from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)