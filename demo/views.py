from django.shortcuts import render
from django.http import HttpResponse
from .models import Course


# Create your views here.

def welcome(request):
    return HttpResponse("<h2>Welcome To Demo Application!</h2>")


def intr(request):
    return render(request, 'intr.html')


def display_course(request):
    c = Course("Python Programming", 40, 5000, ["Language", "Library", "Django"])
    return render(request, 'display_course.html', {"course": c})


def list_courses(request):
    courses = [Course("Python Programming", 40, 5000),
               Course("Java SE", 40, 5000),
               Course("C Programming", 30, 3000)]
    return render(request, 'list_courses.html', {"courses": courses})
