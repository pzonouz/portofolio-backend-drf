from django.urls import path

from projects.views import ProjectView


urlpatterns = [path("", ProjectView.as_view())]
