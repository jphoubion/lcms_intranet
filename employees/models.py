from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# from datetime import datetime


class Companies(models.Model):
    name = models.CharField(max_length=40, verbose_name="Nom")
    legal_form = models.CharField(max_length=10, verbose_name="Forme juridique")

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Companies'
    def __str__(self):
        return f"{self.name} {self.legal_form}"

class CategoryEmployees(models.Model):
    name = models.CharField(max_length=20, default='Administratif', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Employees(models.Model):
    lastname = models.CharField(max_length=100, verbose_name='Nom', default='Dupont')
    firstname = models.CharField(max_length=25, verbose_name='Prénom', default='Dupont')
    company = models.ForeignKey(Companies, verbose_name="Société", related_name="company", on_delete=models.CASCADE)
    category_employees = models.ForeignKey(CategoryEmployees, verbose_name='Catégorie', related_name='category', on_delete=models.CASCADE)
    starting_date = models.DateField(verbose_name="Date d'entrée", null=True, blank=True)
    ending_date = models.DateField(verbose_name="Date de fin", null=True, blank=True)
    has_selection_medical = models.BooleanField(verbose_name="Sélect. médic.", default=False, blank=False)
    selection_medical_start = models.DateField(verbose_name="Date de fin", null=True, blank=True)
    selection_medical_end = models.DateField(verbose_name="Date de fin", null=True, blank=True)
    selection_medical_remind_date = models.DateField(verbose_name="Date de fin", null=True, blank=True)
    picture = models.ImageField(upload_to='employees_pictures', verbose_name="Photo", blank=True, null=True)
    created_by = models.ForeignKey(User, verbose_name='Créé par', related_name='employees', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Créé le', auto_now_add=True)


    class Meta:
        ordering = ('lastname',)
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.lastname} {self.firstname}"
