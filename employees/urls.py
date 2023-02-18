from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
# from .forms import LoginForm

app_name = 'employees'

urlpatterns = [
    path('', views.index, name='index'),
    path('categories', views.categories, name='categories'),
    path('new_category', views.newCategory, name="new_category"),
    path('employees', views.employees, name="employees"),
    path('new_employee', views.newEmployee, name="new_employee"),
    path('edit_employee/<int:pk>', views.editEmployee, name="edit_employee"),
    path('delete_employee/<int:pk>', views.deleteEmployee, name="delete_employee"),
]