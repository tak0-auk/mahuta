# coding: UTF-8
from django.urls import path


from . import views

app_name = 'work'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create', views.WorkCreateView.as_view(), name='create'),
    path('<str:name>/', views.work_index, name='work'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
