
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('search/', views.search),
    path('search_depts/', views.search_depts),
    path('adddept/', views.add_dept),
    re_path('editdept/(?P<id>\d+)/', views.edit_dept),



]
