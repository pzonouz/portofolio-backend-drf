# Generated by Django 4.2.6 on 2023-11-08 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0005_alter_project_name_alter_projectimage_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="banner",
            field=models.BooleanField(default=False),
        ),
    ]
