# Generated by Django 5.1.2 on 2024-12-12 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("planetary", "0010_rename_about_planet_planetarytour_about_planet1_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="planetarytour",
            old_name="about_planet1",
            new_name="about_planet",
        ),
        migrations.RenameField(
            model_name="planetarytour",
            old_name="location_and_orbit1",
            new_name="location_and_orbit",
        ),
    ]
