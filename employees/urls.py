from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
# from .forms import LoginForm

app_name = 'employees'

urlpatterns = [
    path('', views.index, name='index'),

    path('companies', views.companies, name='companies'),
    path('new_company', views.newCompany, name="new_company"),
    path('edit_company/<int:pk>', views.editCompany, name="edit_company"),
    path('delete_company/<int:pk>', views.deleteCompany, name="delete_company"),

    path('categories', views.categories, name='categories'),
    path('new_category', views.newCategory, name="new_category"),
    path('edit_category/<int:pk>', views.editCategory, name="edit_category"),
    path('delete_category/<int:pk>', views.deleteCategory, name="delete_category"),

    path('employees', views.employeesOnCategoryFiltered, name="employees"),
    path('employees_on_category_filtered/<int:pk_category>', views.employeesOnCategoryFiltered, name="employees_on_category_filtered"),
    path('employees_on_company_filtered/<int:pk_company>', views.employeesOnCompanyFiltered, name="employees_on_company_filtered"),
    path('employees_searched_by_name/', views.employeesSearchedByName, name="employees_searched_by_name"),
    path('new_employee', views.newEmployee, name="new_employee"),
    path('edit_employee/<int:pk>', views.editEmployee, name="edit_employee"),
    path('delete_employee/<int:pk>', views.deleteEmployee, name="delete_employee"),
]