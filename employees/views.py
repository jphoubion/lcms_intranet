import datetime

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from employees.models import Employees, CategoryEmployees, Companies
from .forms import NewCategoryEmployeesForm, NewEmployeeForm


@login_required
def index(request):
    """ Displays each emloyee and its category """

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


def newCategory(request):
    """ View to create a new category of employees """

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
        'form': form,})

def editCategory(request, pk):
    category = CategoryEmployees.objects.get(pk=pk)
    print(category, category.id )
    form = NewCategoryEmployeesForm(request.POST or None, instance=category)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/employees/categories')
        else:
            print("form is INVALID")
            print(form.errors.as_data())

    return render(request, 'employees/category_form.html', {
        'category': category,
        'form': form, })

def deleteCategory(request, pk):
    category = CategoryEmployees.objects.get(pk=pk)

    if request.method == "POST":
        category.delete()
        return redirect('/employees/categories')
    return render(request, 'employees/delete_category_form.html', {
        'category': category, })

def employees(request, pk_category):
    if pk_category is None:
        employees = Employees.objects.all()
    else:
        employees = Employees.objects.filter(category_employees_id=pk_category)

    return render(request, 'employees/index.html', {
        'employees': employees,
    })


def newEmployee(request):
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


def editEmployee(request, pk):
    employee = Employees.objects.get(pk=pk)
    creator = User.objects.get(id=employee.created_by.id)
    form = NewEmployeeForm(request.POST or None, request.FILES or None, instance=employee,
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


def deleteEmployee(request, pk):
    employee = Employees.objects.get(pk=pk)

    if request.method == "POST":
        employee.delete()
        return redirect('/employees')
    return render(request, 'employees/delete_employee_form.html', {
        'employee': employee, })