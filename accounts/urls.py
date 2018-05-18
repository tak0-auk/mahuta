# coding: UTF-8
from django.urls import path
from django.contrib.auth import views

app_name = 'account'
urlpatterns = [
    path('logout', views.logout),
]