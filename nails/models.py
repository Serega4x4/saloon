from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class Master(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя мастера')
    second_name = models.CharField(max_length=100, verbose_name='Фамилия мастера')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug',
                            validators=[
                                MinLengthValidator(5, message='Миннимум 5 символов'),
                                MaxLengthValidator(100, message='Максимум 100 символов'),
                            ])
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, blank=True,
                              null=True, verbose_name="Фото мастера")
    about_master = models.TextField(blank=True, verbose_name='О мастере')

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя мастера')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug',
                            validators=[
                                MinLengthValidator(5, message='Миннимум 5 символов'),
                                MaxLengthValidator(100, message='Максимум 100 символов'),
                            ])

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя мастера')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug',
                            validators=[
                                MinLengthValidator(5, message='Миннимум 5 символов'),
                                MaxLengthValidator(100, message='Максимум 100 символов'),
                            ])