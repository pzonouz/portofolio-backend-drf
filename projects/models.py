from django.db import models

from customers.models import Customer


class Project(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="projects"
    )
    year = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.name


class ProjectImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, related_name="images"
    )

    def __str__(self) -> str:
        return self.name
