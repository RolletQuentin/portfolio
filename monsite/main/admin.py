from django.contrib import admin

from main.models import Project


class Project_admin(admin.ModelAdmin):
    list_display = ("name", "type_of_projects")


admin.site.register(Project, Project_admin)
