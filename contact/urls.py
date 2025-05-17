from django.contrib import admin
from django.urls import path
from . import views


app_name='app_contact'
urlpatterns = [
    path("", views.index,name='contact')
]
