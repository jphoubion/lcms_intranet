from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from employees.models import Employees, CategoryEmployees
from .forms import NewCategoryEmployeesForm, NewEmployeeForm

def index(request):
    employees = Employees.objects.all()
    category_employee = CategoryEmployees.objects.all()
    return render(request, 'employees/index.html', {
        'employees': employees,
        'categories': category_employee,
    })

def categories(request):
    """" Get all the categories from the DB """
    categories = CategoryEmployees.objects.all()
    employees = Employees.objects.all()
    return render(request, 'employees/categories.html', {
        'categories': categories,
        'employees': employees,
    })

@login_required
def newCategory(request):
    """ Form to create a new category of employees """

    form = NewCategoryEmployeesForm()

    if request.method == "POST":
        form = NewCategoryEmployeesForm(request.POST)
        if form.is_valid():
            print("from valid")
            form.save()
            return redirect('/employees/categories')
        else:
            print("form is INVALID")
            print(form.errors.as_data())
    else:
        form = NewCategoryEmployeesForm()

    return render(request, 'employees/category_form.html', {
        'form': form,
    })

@login_required
def employees(request):
    employees = Employees.objects.all()
    return render(request, 'employees/employees.html', {
        'employees': employees,
    })

def get_user_id(request):
    current_user = request.user
    print(current_user.id)
    return current_user

def newEmployee(request):
    form = NewEmployeeForm()

    if request.method == "POST":
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            print("from valid")
            form.save()
            return redirect('/employees/employees')
        else:
            print("form is INVALID")
            print(form.errors.as_data())
    else:
        form = NewEmployeeForm()

    return render(request, 'employees/employee_form.html', {
        'form': form,
    
    })