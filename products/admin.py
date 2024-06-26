from django.contrib import admin

from .models import (
    Brand,
    # Carousel,
    Product,
    Description,
    ProductCategoryLevel1,
    ProductCategoryLevel2,
    ProductCategoryLevel3,
    ProductImage,
    ProductVideo,
    Review,
    Specification,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Specification)
class SpecificationModel(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategoryLevel1)
class ProductCategoryL1Admin(admin.ModelAdmin):
    pass


@admin.register(ProductCategoryLevel2)
class ProductCategoryL2Admin(admin.ModelAdmin):
    pass


@admin.register(ProductCategoryLevel3)
class ProductCategoryL3Admin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


# @admin.register(Carousel)
# class CarouselAdmin(admin.ModelAdmin):
#     pass


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductVideo)
class ProductVideoAdmin(admin.ModelAdmin):
    pass
