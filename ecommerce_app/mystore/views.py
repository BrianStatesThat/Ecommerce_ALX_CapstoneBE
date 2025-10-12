from rest_framework import viewsets, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_date')
    serializer_class = ProductSerializer
     permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'category__name']
    filterset_fields = ['category', 'price', 'stock_quantity']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer