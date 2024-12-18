from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, 'зарегистрирован')
                return redirect('main')
            else:
                messages.success('error')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else: 
            messages.success(request,'error')
            return redirect('loginuser')
    else:
        return render(request, 'authentication/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('main')
