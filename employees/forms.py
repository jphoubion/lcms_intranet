from django import forms

from .models import CategoryEmployees

class NewCategoryEmployeesForm(forms.ModelForm):
    class Meta:
        model = CategoryEmployees
        fields = ('name',)

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Nom de la catégorie",
        'class': 'w-full py-4 px-6 rounded-xl'}))
