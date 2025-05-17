from django.contrib import admin
from django.urls import path
from . import views


app_name='app_skill'
urlpatterns = [
    path("", views.index,name='skill')
]
