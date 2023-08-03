# views.py

from rest_framework import viewsets
from rest_framework.response import Response
from .models import PerevalAdd, PerevalImages, User
from .serializers import (
    PerevalAddSerializer,
    PerevalImagesSerializer,
    UserSerializer,
    PerevalAddCreateSerializer,
)


class PerevalAddViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalAddSerializer

    def create(self, request, *args, **kwargs):
        # Используйте PerevalAddCreateSerializer при создании новой записи
        serializer = PerevalAddCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        # Вы можете выполнить дополнительные действия здесь, если необходимо
        # ...

        return Response(PerevalAddSerializer(instance).data)


class PerevalImagesViewSet(viewsets.ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = PerevalImagesSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
