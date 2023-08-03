from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import APIException
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
        serializer = PerevalAddCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            instance = serializer.save()
        except Exception as e:
            raise APIException(detail="Ошибка при выполнении операции", code=500)

        response_data = {
            'status': 200,  # Код HTTP успешного ответа
            'message': 'Отправлено успешно',
            'id': instance.pk,  # id вставленной записи
        }

        return Response(response_data, status=200)  # Ответ с данными о статусе и id

    def handle_exception(self, exc):
        if isinstance(exc, APIException):
            return Response({'status': exc.status_code, 'message': exc.detail}, status=exc.status_code)

        return super().handle_exception(exc)


class PerevalImagesViewSet(viewsets.ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = PerevalImagesSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
