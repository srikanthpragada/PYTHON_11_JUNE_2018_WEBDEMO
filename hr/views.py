from django.shortcuts import render, redirect
from .models import Department, Employee
from .forms import AddDeptForm


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
