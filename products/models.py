from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    preamble = models.TextField(null=True, blank=True)
    image_large = models.ImageField()
    image_small = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField()
    slug = models.CharField(max_length=255, null=True, unique=True)
    preamble = models.TextField()
    categoryLevel3 = models.ForeignKey(
        "ProductCategoryLevel3", on_delete=models.PROTECT, related_name="products"
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, null=True, related_name="products"
    )

    def __str__(self) -> str:
        return self.name


class Description(models.Model):
    field = models.TextField()
    products = models.ManyToManyField(Product, related_name="descriptions")

    def __str__(self) -> str:
        return self.field


class Specification(models.Model):
    field = models.TextField()
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.field


class Review(models.Model):
    field = models.TextField()
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.field


class ProductCategoryLevel1(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)
    slug = models.CharField(max_length=255)
    banner = models.ForeignKey(
        "Banner", on_delete=models.SET_NULL, null=True, related_name="product_level_1s"
    )

    def __str__(self) -> str:
        return self.name


class ProductCategoryLevel2(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    slug = models.CharField(max_length=255)
    parent = models.ForeignKey(
        ProductCategoryLevel1, on_delete=models.PROTECT, related_name="children"
    )

    def __str__(self) -> str:
        return self.name


class ProductCategoryLevel3(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    slug = models.CharField(max_length=255)
    parent = models.ForeignKey(
        ProductCategoryLevel2, on_delete=models.PROTECT, related_name="children"
    )

    def __str__(self) -> str:
        return self.name


class Carousel(models.Model):
    description = models.TextField(null=True, blank=True)
    title = models.CharField(null=True, max_length=256, blank=True)
    image = models.ImageField()
    name = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name


class Banner(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
