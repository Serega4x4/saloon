# Generated by Django 4.2.1 on 2024-05-19 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nails', '0007_alter_master_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='master',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='nails.tagmaster'),
        ),
    ]