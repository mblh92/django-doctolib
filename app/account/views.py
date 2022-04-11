from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def account_pro(request):
    return render(request, "account/pro.html")


def account_client(request):
    return render(request, "account/particulier.html")
