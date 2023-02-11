from django.shortcuts import render, redirect
from .forms import SignupForm


def index(request):
    return render(request, 'core/index.html')


def signup(request):
    print("signup request")
    if request.method == 'POST':
        print("POST request")
        form = SignupForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect('/login/')
        else:
            print("form is INVALID")
            print(form.errors.as_data())
    else:
        print("GET Request")
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })