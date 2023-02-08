from django.contrib.auth.models import User
from django.db import models

class CategoryEmployees(models.Model):
    name = models.CharField(max_length=20, default='Administratif')

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Employees(models.Model):
    lastname = models.CharField(max_length=100, null=True, blank=True, default='Dupont')
    firstname = models.CharField(max_length=25, null=True, blank=True, default='Dupont')
    category_employees = models.ForeignKey(CategoryEmployees, related_name='category', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='employees', on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('lastname',)
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.lastname} {self.firstname}"
