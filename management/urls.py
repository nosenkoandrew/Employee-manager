from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('employee_list/', views.list_view, name='employee_list'),
]
