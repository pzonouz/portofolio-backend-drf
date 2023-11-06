from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    BannersSerializer,
    BrandSerializer,
    CarouselSerializer,
    ProductCategoryLevel1Serializer,
    ProductCategoryLevel2Serializer,
    ProductCategoryLevel3Serializer,
    ProductSerializer,
    ProductsSimpleSerializer,
    ProductsSimpleSerializer,
)
from .models import (
    Banner,
    Brand,
    Carousel,
    Product,
    ProductCategoryLevel1,
    ProductCategoryLevel2,
    ProductCategoryLevel3,
)


class ProductsView(ListAPIView, RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSimpleSerializer


class ProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsByL3View(ListAPIView):
    serializer_class = ProductsSimpleSerializer

    def get_queryset(self):
        return Product.objects.filter(categoryLevel3__id=self.kwargs["id"])


class ProductsByL2View(ListAPIView):
    serializer_class = ProductsSimpleSerializer

    def get_queryset(self):
        return Product.objects.filter(categoryLevel3__parent__id=self.kwargs["id"])


class ProductsByL1View(ListAPIView):
    serializer_class = ProductsSimpleSerializer

    def get_queryset(self):
        return Product.objects.filter(
            categoryLevel3__parent__parent__id=self.kwargs["id"]
        )


class Level3View(RetrieveAPIView):
    serializer_class = ProductCategoryLevel3Serializer
    queryset = ProductCategoryLevel3.objects.all()


class Level2View(RetrieveAPIView):
    serializer_class = ProductCategoryLevel2Serializer
    queryset = ProductCategoryLevel2.objects.all()


class Level1View(RetrieveAPIView):
    serializer_class = ProductCategoryLevel1Serializer
    queryset = ProductCategoryLevel1.objects.all()


class ProductCategoryLevel1View(ListAPIView):
    queryset = ProductCategoryLevel1.objects.all()
    serializer_class = ProductCategoryLevel1Serializer


class BrandsView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductsByBrandView(ListAPIView):
    serializer_class = ProductsSimpleSerializer

    def get_queryset(self):
        return Product.objects.filter(brand__id=self.kwargs["id"])


class CarouselView(ListAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer


class BannersView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannersSerializer
