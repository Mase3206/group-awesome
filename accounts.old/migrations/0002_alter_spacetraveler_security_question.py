# Generated by Django 5.1.2 on 2024-11-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spacetraveler',
            name='security_question',
            field=models.IntegerField(choices=[(0, 'What was the name of your first pet?'), (1, 'What street did you grow up on?'), (2, "What is your mother's maiden name?"), (3, 'Where was your first date?'), (4, 'How many fingers am I holding up?')], null=True),
        ),
    ]