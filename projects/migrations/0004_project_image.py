# Generated by Django 4.2.6 on 2023-11-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_rename_projectsimage_projectimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
