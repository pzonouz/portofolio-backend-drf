from .views import BrandsView, ProductCategoryLevel1View, ProductsView, ProductView

from django.urls import path

urlpatterns = [
    path("", ProductsView.as_view()),
    path("slug/<slug>/", ProductView.as_view()),
    path("classification/", ProductCategoryLevel1View.as_view()),
    path("brands/", BrandsView.as_view()),
]
