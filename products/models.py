from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    preamble = models.TextField(null=True, blank=True)
    image_large = models.ImageField()
    image_small = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.name


PART = "Pt"
SERVICE = "Sr"
CLASS = "Cl"

PRODUCT_TYPE = [(PART, "PART"), (SERVICE, "SERVICE"), (CLASS, "CLASS")]


class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    preamble = models.TextField()
    carousel = models.BooleanField(default=False)
    productType = models.CharField(max_length=255, choices=PRODUCT_TYPE, default=PART)
    image = models.ImageField(null=True, blank=True)
    categoryLevel3 = models.ForeignKey(
        "ProductCategoryLevel3", on_delete=models.PROTECT, related_name="products"
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, null=True, related_name="products"
    )

    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField()
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="images"
    )

    def __str__(self) -> str:
        return self.name


class ProductVideo(models.Model):
    name = models.CharField(max_length=255, unique=True)
    video = models.FileField(max_length=255)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="videos"
    )

    def __str__(self) -> str:
        return self.name


class Description(models.Model):
    field = models.TextField(unique=True)
    products = models.ManyToManyField(Product, related_name="descriptions")

    def __str__(self) -> str:
        return self.field


class Specification(models.Model):
    field = models.TextField(unique=True)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.field


class Review(models.Model):
    field = models.TextField(unique=True)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.field


class ProductCategoryLevel1(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    image = models.ImageField(null=True, blank=True)
    banner = models.BooleanField(default=False)
    productType = models.CharField(max_length=255, choices=PRODUCT_TYPE, default=PART)

    def __str__(self) -> str:
        return self.name


class ProductCategoryLevel2(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    productType = models.CharField(max_length=255, choices=PRODUCT_TYPE, default=PART)
    parent = models.ForeignKey(
        ProductCategoryLevel1, on_delete=models.PROTECT, related_name="children"
    )

    def __str__(self) -> str:
        return self.name


class ProductCategoryLevel3(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    productType = models.CharField(max_length=255, choices=PRODUCT_TYPE, default=PART)
    parent = models.ForeignKey(
        ProductCategoryLevel2, on_delete=models.PROTECT, related_name="children"
    )

    def __str__(self) -> str:
        return self.name
