from rest_framework.generics import ListAPIView, RetrieveAPIView
from projects.serializers import ProjectSerializer
from projects.models import Project


class ProjectsView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectBannersView(ListAPIView):
    queryset = Project.objects.filter(banner=True)
    serializer_class = ProjectSerializer
