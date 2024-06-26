from rest_framework.generics import ListAPIView, RetrieveAPIView

# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.db.models import Q


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
    Brand,
    # Carousel,
    Product,
    ProductCategoryLevel1,
    ProductCategoryLevel2,
    ProductCategoryLevel3,
)


class PartsView(ListAPIView):
    queryset = Product.objects.filter(productType="Pt")
    serializer_class = ProductsSimpleSerializer


class ProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSimpleSerializer


class ServicesView(ListAPIView):
    queryset = Product.objects.filter(productType="Sr")
    serializer_class = ProductsSimpleSerializer


class CLassesView(ListAPIView):
    queryset = Product.objects.filter(productType="Cl")
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
        return Product.objects.filter(
            Q(categoryLevel3__parent__id=self.kwargs["id"])
            | Q(categoryLevel2__id=self.kwargs["id"])
        )


class ProductsByL1View(ListAPIView):
    serializer_class = ProductsSimpleSerializer

    def get_queryset(self):
        return Product.objects.filter(
            Q(categoryLevel3__parent__parent__id=self.kwargs["id"])
            | Q(categoryLevel1__id=self.kwargs["id"])
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


class PartCategoryLevel1View(ListAPIView):
    queryset = ProductCategoryLevel1.objects.filter(productType="Pt")
    serializer_class = ProductCategoryLevel1Serializer


class ClassCategoryLevel1View(ListAPIView):
    queryset = ProductCategoryLevel1.objects.filter(productType="Cl")
    serializer_class = ProductCategoryLevel1Serializer


class ServiceCategoryLevel1View(ListAPIView):
    queryset = ProductCategoryLevel1.objects.filter(productType="Sr")
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
    queryset = Product.objects.filter(carousel=True)
    serializer_class = CarouselSerializer


class BannersView(ListAPIView):
    queryset = ProductCategoryLevel1.objects.filter(banner=True)
    serializer_class = BannersSerializer
