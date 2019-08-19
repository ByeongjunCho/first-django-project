from django.urls import path

# 현재 app(directory)의 views.py
from . import views

urlpatterns = [
    path('push/', views.push),
    path('pull/', views.pull),
]