import datetime

from django import forms
from django.contrib.auth.models import User
from .models import DocumentCategories, Documents

class NewDocumentCategoryForm(forms.ModelForm):
    class Meta:
        model = DocumentCategories
        fields = ('name', 'description', 'parent_id')

    # get all existing categories to be able to choose a parent if needed
    all_categories = DocumentCategories.objects.all()
    print(all_categories)

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Nom de la catégorie",
        'class': 'w-full py-4 px-6  bg-slate-500 text-slate-100'}))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "Description",
        'class': 'w-full py-4 px-6  bg-slate-500 text-slate-100'}))
    parent_id = forms.ModelChoiceField(queryset=all_categories, widget=forms.Select(attrs={
        'placeholder': "Catégorie parente",
        'class': 'w-full py-4 px-6  bg-slate-500 text-slate-100'}),
        required=False)