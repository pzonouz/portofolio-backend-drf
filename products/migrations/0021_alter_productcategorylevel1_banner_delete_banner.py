# Generated by Django 4.2.6 on 2023-11-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0020_product_carousel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productcategorylevel1",
            name="banner",
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name="Banner",
        ),
    ]
