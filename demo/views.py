from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Course
from datetime import datetime, timedelta

blogs = [
    (1, 'Python', 'Getting Started With Python', "url"),
    (2, 'Python', 'How to use Requests Library', "url"),
    (3, 'C#', 'Using Generics', "url"),
]


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


# views related to sessions demo

def add_lang(request):
    if request.method == "GET":
        return render(request, 'add_lang.html')
    else:
        # add lang to langs list in session
        lang = request.POST["lang"]
        if 'langs' in request.session:
            langs = request.session["langs"]
            langs.append(lang)
            request.session["langs"] = langs
        else:
            request.session['langs'] = [lang]  # add key langs to session

        return HttpResponseRedirect("/demo/listlangs")


def list_langs(request):
    return render(request, 'list_langs.html', {"langs": request.session["langs"]})


# views related to cookies demo

def list_blogs(request):
    # get lang from cookie
    if 'lang' in request.COOKIES:  # is cookie with name lang present
        lang = request.COOKIES["lang"]
        return HttpResponse("<h2>Blogs on %s</h2" % (lang))
    else:
        return HttpResponseRedirect("/demo/select_lang")


def select_lang(request):
    return render(request, 'select_lang.html')


def save_lang(request):
    lang = request.POST["lang"]
    resp = HttpResponseRedirect("/demo/listblogs/")
    resp.set_cookie("lang", lang,
                    expires=datetime.now() + timedelta(days=7))
    return resp
