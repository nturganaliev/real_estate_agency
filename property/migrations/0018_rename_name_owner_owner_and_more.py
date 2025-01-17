# Generated by Django 4.1.7 on 2023-02-22 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20230222_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='name',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='pure_phone',
            new_name='owner_pure_phone',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='phone_number',
            new_name='owners_phonenumber',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='master',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
