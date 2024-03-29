# Generated by Django 5.0.1 on 2024-01-06 06:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_orders_order_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orders",
            old_name="value",
            new_name="order_value",
        ),
        migrations.AlterField(
            model_name="customer",
            name="number",
            field=models.IntegerField(max_length=12),
        ),
        migrations.AlterField(
            model_name="orders",
            name="order_date",
            field=models.CharField(max_length=11),
        ),
    ]
