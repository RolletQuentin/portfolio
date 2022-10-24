from atexit import register
from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.models import Project


def home(request):
    return render(request, "main/home.html")


def cv(request):
    return render(request, "main/cv.html")


def portfolio(request):
    def build_django_list(n):
        res = ""
        for i in range(n):
            res += f"{i}"
        return res

    type_of_projects = ["Web", "Python"]
    projects = []
    for type_of_project in type_of_projects:
        projects.append(Project.objects.all().filter(type_of_projects=type_of_project))
    return render(
        request,
        "main/portfolio.html",
        {
            "projects": projects,
            "type_of_projects": type_of_projects,
            "list": build_django_list(len(type_of_projects)),
        },
    )


def project_details(request, id):
    project = Project.objects.get(id=id)
    return render(
        request,
        "main/project_details.html",
        {"id": id, "project": project},
    )


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")


def redirect_view(request):
    response = redirect("/portfolio")
    return response
