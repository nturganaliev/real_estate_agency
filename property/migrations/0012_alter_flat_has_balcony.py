# Generated by Django 4.1.7 on 2023-02-20 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20230219_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='has_balcony',
            field=models.BooleanField(db_index=True, null=True, verbose_name='Наличие балкона'),
        ),
    ]
