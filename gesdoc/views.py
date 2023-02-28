from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    """ Displays index page of GesDoc """

    return render(request, 'gesdoc/index.html')
