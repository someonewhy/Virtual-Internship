from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerevalAddViewSet, PerevalImagesViewSet, UserViewSet

router = DefaultRouter()
router.register(r'perevals', PerevalAddViewSet, basename='perevals')
router.register(r'images', PerevalImagesViewSet, basename='images')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/perevals/get_perevals_by_user_email/', PerevalAddViewSet.as_view({'get': 'get_perevals_by_user_email'}), name='perevals-by-user-email'),
    # другие URL-шаблоны для других эндпоинтов, если они есть
]
