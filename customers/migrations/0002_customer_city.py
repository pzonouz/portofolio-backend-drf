# Generated by Django 4.2.6 on 2023-11-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="city",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
