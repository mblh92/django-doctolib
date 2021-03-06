from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect


# Create your views here.

def login_user(request):
    if not request.user.is_anonymous:
        return redirect("account_client" if request.user.role == 'PARTICULAR' else "account_pro")

    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                if user.role == 'PARTICULAR':
                    return redirect('/account/client')
                elif user.role == 'PROFESSIONAL':
                    return redirect('/account/pro')
        message = 'Identifiants invalides.'
    return render(request, "login/index.html", context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('/')
