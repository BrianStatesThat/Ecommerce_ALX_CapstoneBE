from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from .filters import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for products.
    Only authenticated users can create, update, or delete products.
    Supports search, filtering, and pagination.
    """
    queryset = Product.objects.all().order_by('-created_date')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'category__name']
    filterset_class = ProductFilter

    def get_permissions(self):
        """
        Customize permissions: allow read-only access to unauthenticated users.
        """
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        """
        Custom create method with explicit error handling.
        """
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        """
        Optionally associate the product with the authenticated user.
        """
        serializer.save()

    def update(self, request, *args, **kwargs):
        """
        Custom update method with validation feedback.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if not serializer.is_valid():
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_update(serializer)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for product categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    Handles listing and creating reviews for products.
    Only authenticated users can create reviews.
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Optionally filter reviews by product ID from the URL.
        """
        product_id = self.kwargs.get('product_pk') or self.request.query_params.get('product')
        queryset = Review.objects.all()
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        return queryset.order_by('-created_at')

    def perform_create(self, serializer):
        """
        Associate the review with the authenticated user and product.
        """
        product_id = self.kwargs.get('product_pk') or self.request.data.get('product')
        serializer.save(user=self.request.user, product_id=product_id)