from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/login/', CustomUserViewSet.as_view({'post': 'login'}), name='customuser-login'),
    path('users/register/', CustomUserViewSet.as_view({'post': 'register'}), name='customuser-register'),
    path('products/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
]
