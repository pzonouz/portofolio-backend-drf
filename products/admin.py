from django.contrib import admin

from .models import (
    Brand,
    Product,
    Description,
    ProductCategoryLevel1,
    ProductCategoryLevel2,
    ProductCategoryLevel3,
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
