Установка и запуск
Клонируйте репозиторий с помощью команды:
git clone <URL репозитория>
Установите зависимости:
pip install -r requirements.txt
Создайте и примените миграции:
python manage.py makemigrations
python manage.py migrate
Создайте суперпользователя (если необходимо):
python manage.py createsuperuser
Запустите сервер разработки:
python manage.py runserver
API Endpoints
GET /api/perevals/: Получить список всех перевалов.
GET /api/perevals/<id>/: Получить информацию о конкретном перевале.
POST /api/perevals/: Добавить новый перевал в базу данных.
PUT /api/perevals/<id>/: Отредактировать существующий перевал (если статус "new").
DELETE /api/perevals/<id>/: Удалить перевал (если статус "new").
GET /api/perevals/get_perevals_by_user_email/: Получить список перевалов, отправленных пользователем с указанным email.
Модели данных
Модель PerevalAdd
Описание модели PerevalAdd:

title: Название перевала (CharField).
beautyTitle: Красивое название перевала (CharField).
other_titles: Другие названия перевала (CharField).
connect: Описание перевала (TextField).
level_winter: Уровень сложности зимой (CharField).
level_summer: Уровень сложности летом (CharField).
level_autumn: Уровень сложности осенью (CharField).
level_spring: Уровень сложности весной (CharField).
coords: Координаты перевала (ForeignKey to Coords model).
status: Статус модерации (CharField).
date_added: Дата добавления (DateField).
add_time: Время добавления (TimeField).
users: Пользователи, связанные с перевалом (ManyToManyField to User model).
Модель Coords
Описание модели Coords:

latitude: Широта (FloatField).
longitude: Долгота (FloatField).
height: Высота (IntegerField).
Модель PerevalImages
Описание модели PerevalImages:

pereval: Связь с перевалом (ForeignKey to PerevalAdd model).
title: Название изображения (CharField).
date_added: Дата добавления (DateField).
img: Изображение (ImageField).
Модель PerevalUser
Описание модели PerevalUser:

user: Пользователь (ForeignKey to User model).
pereval: Перевал (ForeignKey to PerevalAdd model).
Авторы
Автор 1
Автор 2
