from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ServiceForm
from .forms import ProfileForm
from .models import Services
from register.models import User
from booking.models import Booking


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

    profile_form = ProfileForm(instance=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Votre profil a bien été mis à jour')
            return redirect('account_pro')
        messages.error(request, profile_form.errors)

    return render(request, "account/profile_pro.html", context={'form': profile_form})

@login_required
def account_client(request):
    bookings = Booking.objects.all().filter(user_id=request.user.id)
    if not check_user(request,'PARTICULAR'):
        return redirect('account_pro')
    return render(request, "account/particulier.html", {'bookings': bookings})
@login_required
def account_profil_pro(request):
    if not check_user(request,'PARTICULAR'):
        return redirect('account_pro')
    return render(request, "account/profile_pro.html")


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

def show_all_practicien(request):
    if not check_user(request,'PARTICULAR'):
        return redirect('account_pro')

    practiciens = User.objects.filter(role="PROFESSIONAL")
    return render(request, "account/show_all_practicien.html", context={'practiciens': practiciens})

def show_services(request):
    services = Services.objects.filter(user_id=request.user.id)
    return services

def account_localisation(request):
    return render(request, "account/localisation.html")