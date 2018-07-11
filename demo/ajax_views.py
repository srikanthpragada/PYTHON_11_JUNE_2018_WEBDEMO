from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime
from .models import Department


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def ajax_now(request):
    return HttpResponse(str(datetime.now()))


def ajax_departments(request):
    depts = Department.objects.all().values()  # get queryset of dict objects
    dept_list = list(depts)  # important: convert the QuerySet to a list object
    return JsonResponse(dept_list, safe=False)
