from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {'count' : count })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
        
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form' : form})

    
# def login(request):
#     return render(request, 'login.html')