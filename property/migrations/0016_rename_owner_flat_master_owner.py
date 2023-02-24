# Generated by Django 4.1.7 on 2023-02-22 15:35

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_flat_owner_pure_phone_number_populate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='owner',
            new_name='master',
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(to='property.flat')),
            ],
        ),
    ]
