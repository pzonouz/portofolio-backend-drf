from rest_framework import serializers
from customers.serializers import CustomerSerializer

from projects.models import Project, ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    images = ProjectImageSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"
