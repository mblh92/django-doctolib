from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def register(request):
    if request.method == 'POST':
        pass
    return render(request, "register/index.html")
