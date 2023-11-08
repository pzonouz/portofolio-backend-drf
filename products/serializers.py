from rest_framework import serializers

from .models import (
    Brand,
    # Carousel,
    Description,
    Product,
    ProductCategoryLevel1,
    ProductCategoryLevel2,
    ProductCategoryLevel3,
    ProductImage,
    ProductVideo,
)


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVideo
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    descriptions = DescriptionSerializer(many=True)
    images = ProductImageSerializer(many=True)
    videos = ProductVideoSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductsSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "image", "images", "videos"]


class ProductCategoryLevel3Serializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = ProductCategoryLevel3
        fields = ["id", "name", "productType", "products"]


class ProductCategoryLevel2Serializer(serializers.ModelSerializer):
    children = ProductCategoryLevel3Serializer(many=True)

    class Meta:
        model = ProductCategoryLevel2
        fields = ["id", "name", "productType", "children"]


class ProductCategoryLevel1Serializer(serializers.ModelSerializer):
    children = ProductCategoryLevel2Serializer(many=True)

    class Meta:
        model = ProductCategoryLevel1
        fields = ["id", "name", "productType", "children"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "image"]


class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryLevel1
        fields = ["id", "name", "image"]
