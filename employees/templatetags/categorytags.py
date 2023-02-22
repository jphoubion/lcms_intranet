from django import template
from employees.models import Employees, CategoryEmployees
register = template.Library()

@register.filter
def countEmployeesInCategory(employees, category):
    return employees.filter(category_employees=category).count()