from django.shortcuts import render

def index(request):
    nombres = range(20)
    return render(request, 'dashboard/index.html',{'nombres': nombres})
