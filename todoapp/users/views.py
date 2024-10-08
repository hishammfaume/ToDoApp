from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages

def landing_view(request):
    if request.user.is_authenticated:
        return redirect('tasks:index')
    
    form_login = AuthenticationForm()
    form_register = UserRegisterForm()
    
    if request.method == 'POST':
        # Check if the login form was submitted
        if 'login_form' in request.POST:
            form_login = AuthenticationForm(data=request.POST)
            if form_login.is_valid():
                user = form_login.get_user()
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('tasks:index')
        
        # Check if the register form was submitted
        elif 'register_form' in request.POST:
            form_register = UserRegisterForm(request.POST)
            if form_register.is_valid():
                user = form_register.save()
                login(request, user)
                messages.success(request, 'Account created successfully!')
                return redirect('tasks:index')

    context = {
        'form_login': form_login,
        'form_register': form_register
    }
    return render(request, 'users/landing.html', context)


def logout_view(request):
    logout(request)
    return redirect('landing-page')