from rest_framework import serializers

from .models import (
    Brand,
    Description,
    Product,
    ProductCategoryLevel1,
    ProductCategoryLevel2,
    ProductCategoryLevel3,
)


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    descriptions = DescriptionSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductCategoryLevel3Serializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = ProductCategoryLevel3
        fields = ["id", "name", "products"]


class ProductCategoryLevel2Serializer(serializers.ModelSerializer):
    children = ProductCategoryLevel3Serializer(many=True)

    class Meta:
        model = ProductCategoryLevel2
        fields = ["id", "name", "children"]


class ProductCategoryLevel1Serializer(serializers.ModelSerializer):
    children = ProductCategoryLevel2Serializer(many=True)

    class Meta:
        model = ProductCategoryLevel1
        fields = ["id", "name", "children"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
