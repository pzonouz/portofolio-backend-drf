from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    ProductCategoryLevel1Serializer,
    ProductCategoryLevel2Serializer,
    ProductSerializer,
)
from .models import Product, ProductCategoryLevel1, ProductCategoryLevel2


class ProductsView(ListAPIView, RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"


class ProductCategoryLevel1View(ListAPIView):
    queryset = ProductCategoryLevel1.objects.all()
    serializer_class = ProductCategoryLevel1Serializer
