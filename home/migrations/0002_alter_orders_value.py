# Generated by Django 5.0.1 on 2024-01-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="value",
            field=models.IntegerField(verbose_name=1000),
        ),
    ]
