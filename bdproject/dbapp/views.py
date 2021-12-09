from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def courses_view(request, *args, **kwargs):
    return render(request, "courses.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})