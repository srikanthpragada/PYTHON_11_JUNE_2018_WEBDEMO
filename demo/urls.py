
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('intr/', views.intr),
    path('introduction/', views.intr),
    path('course/', views.display_course),
    path('listcourses/', views.list_courses),

]
