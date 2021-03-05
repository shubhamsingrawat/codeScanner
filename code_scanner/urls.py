from django.contrib import admin
from django.urls import path,include
from code_scanner import views

urlpatterns = [
    path('home/', views.home),
    path('home/search', views.search),
]