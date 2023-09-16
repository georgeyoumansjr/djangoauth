from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, CustomUserCreationForm
from .forms_logout import LogoutForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration if needed
            # Example: login(request, user)
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, './register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return redirect('home')  # Replace 'home' with your app's home page URL name
                return render(request, './dashboard.html')
                # return HttpResponse("Im logged in, World!")
    else:
        form = LoginForm()
        # return HttpResponse("Im logged in, World!")
        return render(request, './login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    # return redirect('login')  # Redirect to the login page
    return redirect('/newDjangoApp/login/')  # Redirect to the login page

def hello_view(request):
    return HttpResponse("Hello, World!")


def user_logout2(request):
    if request.method == 'POST':
        form = LogoutForm(request.POST)
        if form.is_valid():
            logout(request)
            return redirect('login')  # Redirect to the login page after logout
    else:
        form = LogoutForm()
    return render(request, './logout.html', {'form': form})