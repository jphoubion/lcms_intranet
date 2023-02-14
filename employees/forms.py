from django import forms

from .models import CategoryEmployees, Employees, Companies


class NewCategoryEmployeesForm(forms.ModelForm):
    class Meta:
        model = CategoryEmployees
        fields = ('name',)

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Nom de la catégorie",
        'class': 'w-full py-4 px-6 rounded-xl'}))

class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ('lastname',)

    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Nom",
        'class': 'w-full py-4 px-6 rounded-xl'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Prénom",
        'class': 'w-full py-4 px-6 rounded-xl'}))
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), empty_label="Choisissez une société")
    category_employees = forms.ModelChoiceField(queryset=CategoryEmployees.objects.all(),
                                                empty_label="Choisissez une catégorie d'employé")
    starting_date = forms.DateField(widget=forms.TextInput(attrs={
        'placeholder': "Date de début",
        'class': 'w-full py-4 px-6 rounded-xl'}))
    ending_date = forms.DateField(widget=forms.TextInput(attrs={
        'placeholder': "Date de fin",
        'class': 'w-full py-4 px-6 rounded-xl'}))
    # created_by = forms.Select()
    created_at = forms.DateTimeField(widget=forms.TextInput(attrs={
        'placeholder': "Créé le",
        'class': 'w-full py-4 px-6 rounded-xl'}))