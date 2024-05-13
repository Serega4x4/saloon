from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


class Master(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя мастера')
    second_name = models.CharField(max_length=100, blank=True, verbose_name='Фамилия мастера')
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    info = models.TextField(blank=True, verbose_name="О мастере")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, blank=True,
                              null=True, verbose_name="Фото мастера")

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

    class Meta:
        ordering = ['time_create']
        indexes = [
            models.Index(fields=['time_create'])
        ]

    def get_absolute_url(self):
        return reverse('masters', kwargs={'mas_slug': self.slug})


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
