from django .urls import path
from .views import index
from django.contrib import admin
from core import views

urlpatterns = [
    path('', views.index),
]
