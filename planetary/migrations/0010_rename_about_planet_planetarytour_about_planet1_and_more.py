# Generated by Django 5.1.2 on 2024-12-12 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("planetary", "0009_planetarytour_link"),
    ]

    operations = [
        migrations.RenameField(
            model_name="planetarytour",
            old_name="about_planet",
            new_name="about_planet1",
        ),
        migrations.RenameField(
            model_name="planetarytour",
            old_name="location_and_orbit",
            new_name="location_and_orbit1",
        ),
    ]
