# Generated by Django 4.2.6 on 2023-10-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0008_brand_preamble"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="preamble",
            field=models.TextField(blank=True, null=True),
        ),
    ]
