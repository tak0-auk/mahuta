# coding: UTF-8
from django.urls import path


from . import views

app_name = 'work'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create', views.WorkCreateView.as_view(), name='create'),
    path('<str:name>/', views.WorkIndexView.as_view(), name='work'),
    path('<str:name>/edit', views.work_edit, name='edit'),
    path('<str:name>/save', views.work_save, name='save'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
