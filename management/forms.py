from django import forms
from .models import Category, Employee


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'salary', 'parent', 'employee_avatar']
