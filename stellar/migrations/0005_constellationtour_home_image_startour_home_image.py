# Generated by Django 5.1.2 on 2024-12-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stellar", "0004_constellationtour_link_startour_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="constellationtour",
            name="home_image",
            field=models.ImageField(
                default="static/stellar/constellations/BigDipper.jpg",
                upload_to="static",
            ),
        ),
        migrations.AddField(
            model_name="startour",
            name="home_image",
            field=models.ImageField(
                default="static/stellar/constellations/BigDipper.jpg",
                upload_to="static",
            ),
        ),
    ]
