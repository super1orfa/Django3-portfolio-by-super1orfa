from django.shortcuts import render
from .models import Project
# Create your views here.


def home_page(request):
    project_models = Project.objects.all()
    context = {
        "content": "This is My Home Page",
        "project_models": project_models
    }
    return render(request, "home_page.html", context)
