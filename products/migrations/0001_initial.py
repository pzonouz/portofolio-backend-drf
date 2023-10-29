# Generated by Django 4.2.6 on 2023-10-29 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("image", models.ImageField(upload_to="")),
                ("slug", models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategoryLevel1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategoryLevel2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.CharField(max_length=255)),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="children",
                        to="products.productcategorylevel1",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("field", models.TextField()),
                ("rating", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Specification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("field", models.TextField()),
                (
                    "Product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategoryLevel3",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.CharField(max_length=255)),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="children",
                        to="products.productcategorylevel2",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="categoryLevel3",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="products",
                to="products.productcategorylevel3",
            ),
        ),
        migrations.CreateModel(
            name="Description",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("field", models.TextField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
