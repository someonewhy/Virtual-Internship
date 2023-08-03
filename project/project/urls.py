"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from project.base.views import PerevalAddViewSet, PerevalImagesViewSet, UserViewSet

# Создаем роутер для автоматического создания URL-шаблонов для наших viewsets
router = DefaultRouter()
router.register(r'perevals', PerevalAddViewSet, basename='perevals')
router.register(r'images', PerevalImagesViewSet, basename='images')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    # URL-шаблоны для админки Django
    path('admin/', admin.site.urls),

    # URL-шаблоны для API
    path('api/', include(router.urls)),
    path('api/perevals/get_perevals_by_user_email/', PerevalAddViewSet.as_view({'get': 'get_perevals_by_user_email'}), name='perevals-by-user-email'),

    # URL-шаблоны для аутентификации в REST framework (если нужны)
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

