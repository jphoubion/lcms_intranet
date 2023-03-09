from django.contrib import admin
from .models import Companies, Employees, CategoryEmployees

admin.site.register(Companies)
admin.site.register(Employees)
admin.site.register(CategoryEmployees)