# Generated by Django 4.2.6 on 2023-11-08 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0031_product_categorylevel1"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="categoryLevel2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="products.productcategorylevel2",
            ),
        ),
    ]
