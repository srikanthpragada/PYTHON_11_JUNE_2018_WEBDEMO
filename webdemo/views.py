from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h2>Hello, world. This is Django Webdemo Application.</h2>")
