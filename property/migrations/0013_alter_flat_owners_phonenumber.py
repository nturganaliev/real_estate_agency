# Generated by Django 4.1.7 on 2023-02-20 08:06

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_alter_flat_has_balcony'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owners_phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер владельца'),
        ),
    ]
