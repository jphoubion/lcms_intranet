import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from employees.models import Employees, CategoryEmployees, Companies
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
    return current_user

@login_required
def newEmployee(request):
    # form = NewEmployeeForm(initial={'created_by': request.user, 'created_at': datetime.date.today()})

    if request.method == "POST":
        form = NewEmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form_cleaned = form.cleaned_data
            form_cleaned['created_by'] = request.user
            Employees.objects.create(**form_cleaned)
            return redirect('/employees')
        else:
            print("form is INVALID")
            print(request.FILES)
            print(form.errors.as_data())
    else:
        form = NewEmployeeForm(initial={'created_by': request.user,
                                    'created_at': datetime.date.today()})

    return render(request, 'employees/employee_form.html', {
        'form': form,})

@login_required
def editEmployee(request, pk):
    employee = Employees.objects.get(pk=pk)
    creator = User.objects.get(id=employee.created_by.id)
    form = NewEmployeeForm(request.POST or None, request.FILES or None,
                           instance=employee,
                           initial={'created_by': creator})

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/employees')
        else:
            print("form is INVALID")
            print(request.FILES)
            print(form.errors.as_data())
    return render(request, 'employees/employee_form.html', {
        'employee': employee,
        'form': form, })

@login_required
def deleteEmployee(request, pk):
    employee = Employees.objects.get(pk=pk)

    if request.method == "POST":
        employee.delete()
        return redirect('/employees')
    return render(request, 'employees/delete_employee_form.html', {
        'employee': employee, })