from django.contrib import admin
from django.urls import path
from . import views


app_name='app_project'
urlpatterns = [
    path("", views.indexView.as_view(),name='project'),
    path("detail/<slug:slug>", views.detail, name='detail'),
    path('category-<str:category>/',
         views.indexView.as_view(), name='projects_category'),
    path('page-<int:page>/', views.indexView.as_view(), name='project_page'),
]

