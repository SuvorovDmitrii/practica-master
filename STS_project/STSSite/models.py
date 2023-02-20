from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.utils import timezone

class User(AbstractUser):
    patronomyc = models.CharField(max_length=20, verbose_name="Отчество")
    avatar = models.ImageField(upload_to='media/avatars', default='static/default.png')

    class Meta:
        verbose_name_plural = 'Пользователи'

class Uslugi(models.Model):
    name = models.CharField(max_length=25)
    cat = models.CharField(max_length=20, default='кузовные работы')
    class Meta:
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name
class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='Наименование статуса')

    class Meta:
        verbose_name_plural = 'Статусы'


    def __str__(self):
        return self.name

class Order(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Заказчик')
    car = models.CharField(max_length=50, verbose_name='Автомобиль закачика')
    probeg = models.IntegerField(verbose_name='Пробег автомобиля')
    usluga = models.ForeignKey('Uslugi', on_delete=models.CASCADE, verbose_name='Наименование услуги')
    opisanie = models.CharField(max_length=250, verbose_name='Описание заказа', blank=True, null=True)
    sts = models.IntegerField(verbose_name="Номер СТС")
    date_to = models.DateField(default=timezone.now, verbose_name='Дата подачи заявки', blank=True, null=True)
    time_order = models.TimeField(verbose_name="Время посещения СТО")
    date_order = models.DateField(verbose_name="Дата посещения СТО", default=timezone.now)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, default=1, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '{} {}'.format(self.car, self.usluga)



