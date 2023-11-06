from rest_framework.generics import ListAPIView
from projects.serializers import ProjectSerializer
from projects.models import Project


class ProjectView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
