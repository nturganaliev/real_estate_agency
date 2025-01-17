# Generated by Django 4.1.7 on 2023-02-22 15:38

from django.db import migrations


def copy_data_from_flat_to_owner_model(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats_iterator = Flat.objects.iterator()
    while True:
        try:
            flat = flats_iterator.__next__()
            owner, created = Owner.objects.get_or_create(
                name=flat.master,
                phone_number=flat.owners_phonenumber,
                pure_phone=flat.owner_pure_phone,
            )
            owner.flats.add(flat)
            owner.save()
        except StopIteration:
            break


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_rename_owner_flat_master_owner'),
    ]

    operations = [
        migrations.RunPython(copy_data_from_flat_to_owner_model)
    ]
