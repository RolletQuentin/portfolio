from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


class Project(models.Model):
    class TypeOfProject(models.TextChoices):
        WEB = "Web"
        PYTHON = "Python"
        C = "C"
        JAVA = "Java"
        NEXT = "A venir"

    def __str__(self):
        return f"{self.name}"

    name = models.fields.CharField(max_length=100)
    date = models.fields.DateField()
    short_description = models.fields.TextField()
    description = models.fields.TextField()
    image_name = models.fields.CharField(default="default.svg", max_length=100)
    link = models.fields.URLField(null=True, blank=True)
    type_of_projects = models.fields.CharField(
        choices=TypeOfProject.choices, max_length=10, default="Web"
    )


class User(models.Model):
    firstname = models.fields.CharField(max_length=50)
    name = models.fields.CharField(max_length=50)
    mail = models.fields.EmailField()
    password = models.fields.CharField(max_length=50)
