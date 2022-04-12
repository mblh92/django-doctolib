from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

def index(request):
    if not request.user.is_anonymous:
        return redirect("account_client" if request.user.role == 'PARTICULAR' else "account_pro")
    return render(request, "index/index.html")
