from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def check_user(request,role):
    if request.user.role == role:
        return True
    else:
        return False

@login_required
def account_pro(request):
    if not check_user(request,'PROFESSIONAL'):
        return redirect('account_client')
    return render(request, "account/pro.html")

@login_required
def account_client(request):
    if not check_user(request,'PARTICULAR'):
        return redirect('account_pro')
    return render(request, "account/particulier.html")
