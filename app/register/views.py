from django.shortcuts import render, redirect
from register.models import User
from . import forms
from django.contrib.auth import login
from django.conf import settings


# Create your views here.

def register(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "register/index.html", context={'form': form})
