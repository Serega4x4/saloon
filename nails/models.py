from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Master.Status.PUBLISHED)


class Master(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Мастер не активен'
        PUBLISHED = 1, 'Мастер в салоне'

    first_name = models.CharField(max_length=100, verbose_name='Имя мастера')
    second_name = models.CharField(max_length=100, blank=True, verbose_name='Фамилия мастера')
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    info = models.TextField(blank=True, verbose_name="О мастере")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, blank=True,
                              null=True, verbose_name="Фото мастера")
    service = models.ForeignKey('Service', on_delete=models.PROTECT)
    tags = models.ManyToManyField('TagMaster', blank=True, related_name='tags')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

    class Meta:
        ordering = ['time_create']
        indexes = [
            models.Index(fields=['time_create'])
        ]

    def get_absolute_url(self):
        return reverse('masters', kwargs={'master_slug': self.slug})


class Service(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('masters', kwargs={'master_slug': self.slug})


class TagMaster(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})
