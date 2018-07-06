from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Course
import sqlite3
from .forms import AddCourseForm


def add_course_with_form(request):
    message = ""
    if request.method == "POST":
        f = AddCourseForm(request.POST)
        if f.is_valid():
            try:
                con = sqlite3.connect(r"e:\classroom\python\st.db")
                cur = con.cursor()
                row = ( f.cleaned_data['id'], f.cleaned_data['title'],
                        f.cleaned_data['duration'], f.cleaned_data['fee'])
                cur.execute("insert into courses values(?,?,?,?)", row)
                con.commit()
                message = "Added Course Successfully!"
                f = AddCourseForm()   # empty form
            except Exception as ex:
                print("Sorry! Error: ", ex)
                message = "Sorry! Could not add course!"
            finally:
                con.close()

    else:  # get
        f = AddCourseForm()  # create empty form

    return render(request, 'st_add_course_with_form.html', {'form': f, 'message' : message})


def add_course(request):
    message = ""
    con = sqlite3.connect(r"e:\classroom\python\st.db")
    cur = con.cursor()
    if request.method == "POST":
        # take data from POST dict
        row = (request.POST["id"], request.POST["title"],
               request.POST["duration"], request.POST["fee"])
        try:
            cur.execute("insert into courses values(?,?,?,?)", row)
            con.commit()
            message = "Added Course Successfully!"
            # increment id by 1
            id = int(row[0]) + 1
        except Exception as ex:
            print("Sorry! Error: ", ex)
            message = "Sorry! Could not add course!"
        finally:
            con.close()
    else:  # Get
        cur.execute("select max(id) + 1 from courses")
        row = cur.fetchone()
        id = row[0]  # next id

    return render(request, 'st_add_course.html', {"id": id, "message": message})


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
