from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import NewDocumentCategoryForm
from .models import DocumentCategories

@login_required
def index(request, catId=None):
    """ Displays index page of GesDoc with all document categories """
    print(catId)
    if catId is None:
        documentCategories = DocumentCategories.objects.filter(parent_id__isnull=True)
    else:
        documentCategories = DocumentCategories.objects.filter(parent_id__isnull=catId)

    return render(request, 'gesdoc/index.html',
                  {'documentCategories': documentCategories})


def newDocumentCategory(request):
    """ Displays for to create a new document category """

    form = NewDocumentCategoryForm()
    if request.method == "POST":
        form = NewDocumentCategoryForm(request.POST)
        if form.is_valid():
            print("from valid")
            form.save()
            return redirect('/gesdoc/')
        else:
            print("form is INVALID")
            print(form.errors.as_data())
    else:
        form = NewDocumentCategoryForm()

    return render(request, 'gesdoc/document_category_form.html', {
        'form': form, })