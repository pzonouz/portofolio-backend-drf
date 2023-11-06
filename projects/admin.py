from django.contrib import admin

from projects.models import Project, ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    pass
