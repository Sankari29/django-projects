from django.shortcuts import render, redirect
from django.views import View
from .forms import Regform, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

    
class reg(View):
    def get(self, request):
        form = Regform()
        return render(request, 'reg.html', {'form': form})

    def post(self, request):
        form = Regform(request.POST)
        if form.is_valid():
            user= form.save()
            return redirect('/')
        return render(request, 'reg.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
        
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')

@login_required
def home(request):
    return render(request, 'home.html')
