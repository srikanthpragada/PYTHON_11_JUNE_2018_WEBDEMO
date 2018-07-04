
from django.contrib import admin
from django.urls import path
from . import views, st_views

urlpatterns = [
    path('welcome/', views.welcome),
    path('intr/', views.intr),
    path('introduction/', views.intr),
    path('course/', views.display_course),
    path('listcourses/', views.list_courses),
    path('st_addcourse/', st_views.add_course),
    path('st_listcourses/', st_views.list_courses),
    path('st_deletecourse/', st_views.delete_course),


]
