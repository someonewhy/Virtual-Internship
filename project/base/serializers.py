from rest_framework import serializers
from .models import PerevalAdd, PerevalImages, User, PerevalUser, PerevalAreas, Coords

# Сериализатор для модели Coords
class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = "__all__"

# Сериализатор для модели PerevalAdd
class PerevalAddSerializer(serializers.ModelSerializer):
    # Включаем сериализатор для модели Coords внутрь PerevalAddSerializer
    coords = CoordsSerializer()

    class Meta:
        model = PerevalAdd
        fields = (
            "id",
            "title",
            "beautyTitle",
            "other_titles",
            "connect",
            "level_winter",
            "level_summer",
            "level_autumn",
            "level_spring",
            "coords",  # Включаем координаты в сериализацию
            "status",
            "date_added",
            "add_time",
            "users",
        )

# Сериализатор для модели PerevalUser
class PerevalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalUser
        fields = "__all__"

# Сериализатор для модели PerevalAreas
class PerevalAreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAreas
        fields = "__all__"

# Сериализатор для модели PerevalImages
class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = "__all__"

# Сериализатор для модели User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")

# Сериализатор для создания новой записи в модели PerevalAdd
class PerevalAddCreateSerializer(serializers.ModelSerializer):
    # Включаем сериализатор для модели Coords внутрь PerevalAddCreateSerializer
    coords = CoordsSerializer()

    class Meta:
        model = PerevalAdd
        fields = (
            "title",
            "beautyTitle",
            "other_titles",
            "connect",
            "level_winter",
            "level_summer",
            "level_autumn",
            "level_spring",
            "coords",  # Включаем координаты в сериализацию
        )
