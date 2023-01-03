from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

path("",views.project_idex,name="project_index"),
path("",views.project_detail,name="project_detail"),
]