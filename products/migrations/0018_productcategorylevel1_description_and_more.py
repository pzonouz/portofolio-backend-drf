# Generated by Django 4.2.6 on 2023-11-06 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0017_rename_banners_banner"),
    ]

    operations = [
        migrations.AddField(
            model_name="productcategorylevel1",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="productcategorylevel2",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="productcategorylevel3",
            name="description",
            field=models.TextField(null=True),
        ),
    ]
