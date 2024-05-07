from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class Master(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя мастера')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug',
                            validators=[
                                MinLengthValidator(5, message='Миннимум 5 символов'),
                                MaxLengthValidator(100, message='Максимум 100 символов'),
                            ])
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, blank=True,
                              null=True, verbose_name="Фото мастера")
    about_master = models.TextField(blank=True, verbose_name='О мастере')
