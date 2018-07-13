from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import AddDeptForm
from .models import Department, Employee


# Create your views here.

def home(request):
    depts = Department.objects.all()
    emps = Employee.objects.all()
    return render(request, 'home.html', {"depts": depts, "emps": emps})


def add_dept(request):
    if request.method == "POST":
        form = AddDeptForm(request.POST)
        form.save()
        return redirect("/hr/home")
    else:
        form = AddDeptForm()
        return render(request, 'add_dept.html', {'form': form})


def edit_dept(request, id):
    if request.method == "GET":
        dept = Department.objects.get(id=id)
        form = AddDeptForm(instance=dept)
        return render(request, 'edit_dept.html', {'form': form})
    else:  # POST
        dept = Department.objects.get(id=id)
        form = AddDeptForm(request.POST, instance=dept)
        form.save()  # Update
        return redirect("/hr/home")


def search(request):
    return render(request, 'search.html')


def search_depts(request):
    pattern = request.GET["q"]
    #  print(pattern)
    depts = Department.objects.filter(name__contains=pattern).values()
    list_depts = list(depts)
    return JsonResponse(list_depts, safe=False)





