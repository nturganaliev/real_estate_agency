# Generated by Django 2.2.24 on 2023-02-19 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20230219_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='liked',
            new_name='likes',
        ),
    ]