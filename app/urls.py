from django.contrib import admin
from django.urls import path, include
from .views import test

urlpatterns = [
    path('test/', test, 'test'),
]