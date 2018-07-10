
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('adddept/', views.add_dept),
    re_path('editdept/(?P<id>\d+)/', views.edit_dept),



]
