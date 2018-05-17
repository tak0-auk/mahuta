# coding: UTF-8
from django.urls import path

from . import views

app_name = 'tidy'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
