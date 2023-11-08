from django.urls import path

from projects.views import ProjectBannersView, ProjectView, ProjectsView


urlpatterns = [
    path("", ProjectsView.as_view()),
    path("by_id/<pk>/", ProjectView.as_view()),
    path("banners/", ProjectBannersView.as_view()),
]
