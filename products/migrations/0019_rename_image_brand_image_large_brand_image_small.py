# Generated by Django 4.2.6 on 2023-11-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0018_productcategorylevel1_description_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="brand",
            old_name="image",
            new_name="image_large",
        ),
        migrations.AddField(
            model_name="brand",
            name="image_small",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
