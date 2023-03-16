from django.shortcuts import render

from employees.models import Companies, Employees

def index(request):
    companies = Companies.objects.all()
    employees = Employees.objects.all()
    return render(request, 'dashboard/index.html',
                  {'companies': companies,
                   'employees': employees})
