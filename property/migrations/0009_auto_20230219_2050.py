# Generated by Django 2.2.24 on 2023-02-19 17:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20230219_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
