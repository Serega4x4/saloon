# Generated by Django 4.2.1 on 2024-05-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nails', '0003_alter_master_options_master_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
