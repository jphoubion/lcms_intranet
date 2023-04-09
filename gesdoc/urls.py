from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'gesdoc'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:catId>', views.index, name='index_with_parentId'),

    path('new_document_category', views.newDocumentCategory, name='new_document_category'),
    path('edit_document_category', views.newDocumentCategory, name='edit_document_category'),
]