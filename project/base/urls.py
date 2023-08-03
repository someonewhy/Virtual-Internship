from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerevalAddViewSet, PerevalImagesViewSet, UserViewSet

router = DefaultRouter()
router.register(r'perevals', PerevalAddViewSet, basename='perevals')
router.register(r'images', PerevalImagesViewSet, basename='images')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]