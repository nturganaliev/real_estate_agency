import phonenumbers
import phonenumber_field.modelfields

from django.db import migrations


def correct_phonenumbers_format(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if phonenumbers.is_valid_number(phonenumbers.parse(flat.owners_phonenumber, 'RU')):
            flat.owner_pure_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_alter_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(correct_phonenumbers_format)
    ]