# Generated by Django 4.1.7 on 2023-04-04 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="item_count",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="order",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]
