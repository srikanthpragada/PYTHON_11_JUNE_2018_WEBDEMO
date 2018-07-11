
from django.contrib import admin
from django.urls import path
from . import views, st_views, ajax_views

urlpatterns = [
    path('welcome/', views.welcome),
    path('ajax_demo/', ajax_views.ajax_demo),
    path('ajax_now/', ajax_views.ajax_now),
    path('ajax_depts/', ajax_views.ajax_departments),
    path('intr/', views.intr),
    path('introduction/', views.intr),
    path('course/', views.display_course),
    path('listcourses/', views.list_courses),
    path('st_addcourse/', st_views.add_course),
    path('st_listcourses/', st_views.list_courses),
    path('st_deletecourse/', st_views.delete_course),
    path('select_lang/', views.select_lang),
    path('save_lang/', views.save_lang),
    path('listblogs/', views.list_blogs),
    path('addlang/', views.add_lang),
    path('listlangs/', views.list_langs),
    path('st_addcourse_form/', st_views.add_course_with_form),


]
