from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class HotelRooms(models.Model):
    """Номера отеля"""
    title = models.CharField("Название", max_length=500)
    desc = models.CharField("Описание", max_length=5000)
    image = models.ImageField("Фото", upload_to="room/", null=True, blank=True)

    class Meta:
        verbose_name = "Номер отеля"
        verbose_name_plural = "Номера отеля"

    def __str__(self):
        return self.title


class HotelFields(models.Model):
    """Поля номеров"""
    title = models.CharField("Название", max_length=250)
    sub_title = models.CharField("Описание", max_length=250, default='')
    icon = models.CharField("Иконка", max_length=500)
    about_room = models.ForeignKey(
        HotelRooms,
        verbose_name="О номере",
        on_delete=models.CASCADE,
        related_name="about_room"
    )

    class Meta:
        verbose_name = "Поле номеров"
        verbose_name_plural = "Поля номеров"

    def __str__(self):
        return self.title


class RatingsRooms(models.Model):
    """Оценки сервиса номеров"""
    title = models.CharField("Низвание", max_length=250)
    rating = models.FloatField("Оценка", validators=[MinValueValidator(0), MaxValueValidator(10)])
    services = models.ForeignKey(
        HotelRooms,
        verbose_name="Оценка сервиса",
        on_delete=models.CASCADE,
        related_name="services"
    )

    class Meta:
        verbose_name = "Оценка сервиса номеров"
        verbose_name_plural = "Оценки сервиса номеров"

    def __str__(self):
        return self.title


class BookingRoom(models.Model):
    """Модель бронирования номеров"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    entry_date = models.CharField("Дата заезда", max_length=100)
    depart_date = models.CharField("Дата выезда", max_length=100)
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=100)
    comment = models.TextField("Комментарий", max_length=2500, blank=True)
    adult = models.PositiveIntegerField("Взрослые", default=0)
    children = models.PositiveIntegerField("Дети", default=0)
    image = models.ImageField("Фото", upload_to="booking/", null=True, blank=True)
    rooms = models.ForeignKey(
        HotelRooms,
        verbose_name="Заказанный номер",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Забронированный номер"
        verbose_name_plural = "Забронированные номера"

    def __str__(self):
        return self.name
