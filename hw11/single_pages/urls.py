from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "single_pages"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('', views.layout, name = 'layout'),
    path('about_sy/', views.isy, name = 'about_sy'),
    path('about_jh/', views.kjh, name = 'about_jh'),
    path('project/', views.project, name = 'project'),
    path('', views.landing),
]