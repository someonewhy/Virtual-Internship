from django.db import models
from users.models import User

# Определяем список выбора для поля "status" модели PerevalAdd
status_choices = [
    ("new", "новый"),
    ("pending", "модератор взял в работу"),
    ("accepted", "модерация прошла успешно"),
    ("rejected", "модерация прошла, информация не принята"),
]

# Модель Coords представляет собой таблицу с координатами
class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    def __str__(self):
        return f"ID: {self.pk}, Lat: {self.latitude}, Lon: {self.longitude}, Height: {self.height}"

# Модель PerevalAdd представляет собой таблицу в базе данных Django
class PerevalAdd(models.Model):
    title = models.CharField(max_length=255)
    beautyTitle = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField()

    level_winter = models.CharField(max_length=255)
    level_summer = models.CharField(max_length=255)
    level_autumn = models.CharField(max_length=255)
    level_spring = models.CharField(max_length=255)

    # Связываем модель PerevalAdd с моделью Coords через внешний ключ coords
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE, related_name="perevals", null=True, blank=True)

    status = models.CharField(max_length=10, choices=status_choices, default="new")
    date_added = models.DateField(auto_now_add=True)
    add_time = models.TimeField(auto_now_add=True)

    # Поле ManyToMany связывающее модель PerevalAdd с моделью User через промежуточную модель PerevalUser
    users = models.ManyToManyField(User, through='PerevalUser')

    def __str__(self):
        return f"id: {self.pk}, title: {self.title}"

# Модель PerevalUser представляет собой связь между объектами PerevalAdd и User
class PerevalUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pu_user")
    pereval = models.ForeignKey(PerevalAdd, on_delete=models.CASCADE, related_name="pereval")

    def __str__(self):
        return f"id: {self.pk}, username: {self.user}"

# Модель PerevalAreas представляет собой таблицу с областями для каждого объекта PerevalAdd
class PerevalAreas(models.Model):
    pereval = models.ForeignKey(PerevalAdd, on_delete=models.CASCADE, related_name="areas")
    title = models.TextField()

# Модель PerevalImages представляет собой таблицу с изображениями для каждого объекта PerevalAdd
class PerevalImages(models.Model):
    pereval = models.ForeignKey(PerevalAdd, on_delete=models.CASCADE, related_name="photos")
    title = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return f"id: {self.pk}, title: {self.title}"
