# Generated by Django 4.1.7 on 2023-02-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_alter_complaint_flat_alter_complaint_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(blank=True, db_index=True, null=True, verbose_name='Новое здание'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, null=True, related_name='owners', to='property.flat', verbose_name='Квартиры'),
        ),
    ]
