from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Course
import sqlite3


def add_course(request):
    message = ""
    if request.method == "POST":
        # take data from POST dict
        row = (request.POST["id"], request.POST["title"],
               request.POST["duration"], request.POST["fee"])

        con = sqlite3.connect(r"e:\classroom\python\st.db")

        try:
            cur = con.cursor()
            cur.execute("insert into courses values(?,?,?,?)", row)
            con.commit()
            message = "Added Course Successfully!"
        except Exception as ex:
            print("Sorry! Error: ", ex)
            message = "Sorry! Could not add course!"
        finally:
            con.close()

    return render(request, 'st_add_course.html', {"message": message})


def list_courses(request):
    # take data from POST dict
    con = sqlite3.connect(r"e:\classroom\python\st.db")
    rows = None
    try:
        cur = con.cursor()
        cur.execute("select * from courses order by id")
        rows = cur.fetchall()
    except Exception as ex:
        print("Sorry! Error: ", ex)
    finally:
        con.close()

    return render(request, 'st_list_courses.html', {'courses': rows})


def delete_course(request):
    print(request.GET["id"])
    # Delete course with given id

    # redirect to list
    return HttpResponseRedirect("/demo/st_listcourses")
