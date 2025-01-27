from django.shortcuts import redirect, render,HttpResponse
from Student.models import Students
from Student.forms import StudentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .utils import logout_required
from django.views.generic import TemplateView, ListView


# Create your views here.

@logout_required
def user_signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('user_login')
        else:
            messages.error(request, 'Account creation failed')
            return redirect('user_signup')          
    return render(request, 'user_auth/signup.html', context={'form': form})

@logout_required
def user_login(request):
    form = AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'"{user.username}" -Logged in successfully')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('user_login')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('user_login')
    return render(request, 'user_auth/login.html', context={'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('user_login')


# def user_profile(request):
#     students = Students.objects.filter(user=request.user)
#     return render(request, 'user_auth/profile.html', context={'students': students})



