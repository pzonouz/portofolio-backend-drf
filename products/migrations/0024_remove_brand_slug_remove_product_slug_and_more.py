# Generated by Django 4.2.6 on 2023-11-07 16:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0023_productcategorylevel1_producttype_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="brand",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="product",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="productcategorylevel1",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="productcategorylevel2",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="productcategorylevel3",
            name="slug",
        ),
    ]
