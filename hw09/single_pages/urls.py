from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "single_pages"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('', views.layout, name = 'layout'),
    path('isy/', views.isy, name = 'isy'),
    path('kjh/', views.kjh, name = 'kjh'),
    path('project/', views.project, name = 'project'),
]