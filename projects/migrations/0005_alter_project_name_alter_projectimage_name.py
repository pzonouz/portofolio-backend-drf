# Generated by Django 4.2.6 on 2023-11-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0004_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="projectimage",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
