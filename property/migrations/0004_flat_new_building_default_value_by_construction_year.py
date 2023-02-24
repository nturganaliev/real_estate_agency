from django.db import migrations, models


def categorize_building_by_construction_year(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.filter(construction_year__gte=2015)
    for flat in flats:
        flat.new_building = True
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(categorize_building_by_construction_year)
    ]
