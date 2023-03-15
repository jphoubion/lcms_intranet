from django import template
from employees.models import Employees, Companies
register = template.Library()

@register.filter
def countEmployeesInCompany(employees, company):
    print(f"company = {company}")
    print(f"employees = {employees}")
    return employees.filter(company=company).count()