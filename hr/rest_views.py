from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DeptSerializer
from .models import Department
from django.shortcuts import render


def rest_client(request):
    return render(request, 'rest_client.html')


@api_view(['GET', 'POST'])
def rest_depts(request):
    if request.method == "GET":
        depts = Department.objects.all()
        serializer = DeptSerializer(depts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DeptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=204)
        else:
            return Response(status=500)


@api_view(['DELETE','GET','PUT'])
def rest_dept_id(request, id):
    try:
        dept = Department.objects.get(pk=id)
    except:
        return Response(status=404)

    if request.method == "DELETE":
        try:
            dept.delete()
            return Response(status=204)
        except:
            return Response(status=500)
    elif request.method== "GET":
        serializer = DeptSerializer(dept)
        return Response(serializer.data)
    else:
        serializer = DeptSerializer(dept, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)
