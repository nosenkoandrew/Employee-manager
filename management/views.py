from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def home_view(request):
    welcome_message = 'Welcome to Business Manager'
    employees = Employee.objects.all()

    context = {
        'welcome_message': welcome_message,
        'employees': employees,
    }
    return render(request, "management/home.html", context)


def list_view(request):
    title = " Employee List "
    employees = Employee.objects.all()

    context = {
        'welcome_message': title,
        'employees': employees,
    }

    return render(request, "management/employee_list.html", context)

