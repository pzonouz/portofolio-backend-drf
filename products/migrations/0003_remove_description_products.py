# Generated by Django 4.2.6 on 2023-10-30 08:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_descriptions"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="description",
            name="products",
        ),
    ]
