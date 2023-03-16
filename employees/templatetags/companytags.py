from django import template
from employees.models import Employees, Companies
register = template.Library()

@register.filter
def countEmployeesInCompany(employees, company):
    return employees.filter(company=company).count()