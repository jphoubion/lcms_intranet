from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# from datetime import datetime

class CategoryEmployees(models.Model):
    name = models.CharField(max_length=20, default='Administratif', unique=True)
    # employees = models.ManyToOneRel()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Employees(models.Model):
    lastname = models.CharField(max_length=100, verbose_name='Nom', null=True, blank=True, default='Dupont')
    firstname = models.CharField(max_length=25, verbose_name='Prénom', null=True, blank=True, default='Dupont')
    category_employees = models.ForeignKey(CategoryEmployees, verbose_name='Catégorie', related_name='category', on_delete=models.CASCADE)
    starting_date = models.DateField(verbose_name="Date d'entrée")
    ending_date = models.DateField(verbose_name="Date de fin")
    created_by = models.ForeignKey(User, verbose_name='Créé par', related_name='employees', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Créé le', auto_now_add=True)

    class Meta:
        ordering = ('lastname',)
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.lastname} {self.firstname}"
