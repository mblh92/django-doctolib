from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render, redirect

from . import forms


# Create your views here.

def register(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            if user.role == 'PARTICULAR':
                return redirect(settings.LOGIN_REDIRECT_URL + '/client')
            elif user.role == 'PROFESSIONAL':
                return redirect(settings.LOGIN_REDIRECT_URL + '/pro')

    return render(request, "register/index.html", context={'form': form})
