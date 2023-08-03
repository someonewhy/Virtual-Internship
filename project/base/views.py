from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from django.core.exceptions import ObjectDoesNotExist
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

    @action(detail=True, methods=['get'])
    def get_pereval_by_id(self, request, pk=None):
        pereval = get_object_or_404(PerevalAdd, pk=pk)
        serializer = PerevalAddSerializer(pereval)
        return Response(serializer.data)

    def handle_exception(self, exc):
        if isinstance(exc, APIException):
            return Response({'status': exc.status_code, 'message': exc.detail}, status=exc.status_code)

        return super().handle_exception(exc)

    @action(detail=True, methods=['put'])
    def edit_pereval(self, request, pk=None):
        pereval = get_object_or_404(PerevalAdd, pk=pk)

        # Проверяем, что статус перевала "new"
        if pereval.status != 'new':
            return Response({'state': 0, 'message': 'Нельзя редактировать запись, которая уже взята в работу.'},
                            status=400)

        # Десериализуем данные и проверяем их валидность
        serializer = PerevalAddCreateSerializer(pereval, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        try:
            instance = serializer.save()
        except Exception as e:
            raise APIException(detail="Ошибка при выполнении операции", code=500)

        return Response({'state': 1, 'message': 'Запись успешно отредактирована.'}, status=200)

    def handle_exception(self, exc):
        if isinstance(exc, APIException):
            return Response({'status': exc.status_code, 'message': exc.detail}, status=exc.status_code)

        return super().handle_exception(exc)

    @action(detail=False, methods=['get'])
    def get_perevals_by_user_email(self, request):
        email = request.query_params.get('email')

        if not email:
            return Response({'state': 0, 'message': 'Не указан email пользователя.'}, status=400)

        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return Response({'state': 0, 'message': 'Пользователь с указанным email не найден.'}, status=404)

        perevals = PerevalAdd.objects.filter(users=user)

        serializer = PerevalAddSerializer(perevals, many=True)
        return Response(serializer.data, status=200)


class PerevalImagesViewSet(viewsets.ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = PerevalImagesSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
