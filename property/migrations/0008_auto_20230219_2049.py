# Generated by Django 2.2.24 on 2023-02-19 17:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
