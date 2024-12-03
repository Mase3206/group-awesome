# Generated by Django 5.1.2 on 2024-12-02 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StarTour",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("type", models.CharField(max_length=100)),
                ("distance", models.CharField(max_length=100)),
                ("temp", models.CharField(max_length=100)),
                ("about1", models.CharField(max_length=200)),
                ("about2", models.CharField(max_length=200)),
                ("about3", models.CharField(max_length=200)),
                ("length", models.PositiveIntegerField()),
                ("num_people", models.PositiveIntegerField()),
            ],
        ),
    ]