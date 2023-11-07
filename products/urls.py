from .views import (
    BannersView,
    BrandView,
    BrandsView,
    CarouselView,
    ClassCategoryLevel1View,
    Level1View,
    Level2View,
    Level3View,
    PartCategoryLevel1View,
    ProductView,
    ProductsByBrandView,
    ProductsByL1View,
    ProductsByL2View,
    ProductsByL3View,
    ProductsView,
    ServiceCategoryLevel1View,
)

from django.urls import path

urlpatterns = [
    path("", ProductsView.as_view()),
    path("by_id/<pk>/", ProductView.as_view()),
    path("by_level3/<id>/", ProductsByL3View.as_view()),
    path("by_level2/<id>/", ProductsByL2View.as_view()),
    path("by_level1/<id>/", ProductsByL1View.as_view()),
    path("level3/<pk>/", Level3View.as_view()),
    path("level2/<pk>/", Level2View.as_view()),
    path("level1/<pk>/", Level1View.as_view()),
    path("parts_classification/", PartCategoryLevel1View.as_view()),
    path("services_classification/", ServiceCategoryLevel1View.as_view()),
    path("classes_classification/", ClassCategoryLevel1View.as_view()),
    path("brands/", BrandsView.as_view()),
    path("brand/<pk>/", BrandView.as_view()),
    path("by_brand/<id>/", ProductsByBrandView.as_view()),
    path("carousel/", CarouselView.as_view()),
    path("banners/", BannersView.as_view()),
]
