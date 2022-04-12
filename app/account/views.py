from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ServiceForm
from .models import Services


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


@login_required
def account_services(request):
    if not check_user(request,'PROFESSIONAL'):
        return redirect('account_client')
    form = ServiceForm()
    services = show_services(request)
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.user_id = request.user.id
            service.save()
            messages.success(request, "Service ajouté avec succès")
            return redirect("account_services")
        messages.error(request, "Votre service n'a pas été ajouté")
        messages.error(request, form.errors)
    return render(request, "account/services.html", context={'form': form, 'services': services})

def show_services(request):
    services = Services.objects.filter(user_id=request.user.id)
    return services