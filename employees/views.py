from django.shortcuts import render

from employees.models import Employees, CategoryEmployees

def index(request):
    employees = Employees.objects.all()
    category_employee = CategoryEmployees.objects.all()
    return render(request, 'employees/index.html', {
        'employees': employees,
        'categories' : category_employee,
    })
