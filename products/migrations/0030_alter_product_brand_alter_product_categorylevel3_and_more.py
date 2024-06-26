# Generated by Django 4.2.6 on 2023-11-08 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0029_alter_brand_name_alter_description_field_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="products.brand",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="categoryLevel3",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="products.productcategorylevel3",
            ),
        ),
        migrations.AlterField(
            model_name="productcategorylevel3",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="children",
                to="products.productcategorylevel2",
            ),
        ),
    ]
