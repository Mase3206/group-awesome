# Generated by Django 5.1.2 on 2024-12-02 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planetary", "0004_planetarytour_about_planet_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="planetarytour",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="planetary_tours/"
            ),
        ),
    ]
