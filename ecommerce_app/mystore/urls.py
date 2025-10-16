from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ReviewViewSet
from users.views import UserViewSet  # Import from users app

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)
router.register(r'reviews', ReviewViewSet, basename='review')  # Add this line

urlpatterns = [
    path('', include(router.urls)),
]