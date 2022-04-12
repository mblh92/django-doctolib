from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BookingForm

# Create your views here.

def check_user(request):
    if request.user.role == "PARTICULAR":
        return True
    else:
        return False

@login_required
def booking(request):
    if check_user(request):
        user_id = request.user.id
        form = BookingForm()
        message = ""
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user_id = user_id
                obj.save()
                message = "Booking Successful"
        return render(request, 'booking/index.html', {'form': form, "message": message})
    else:
        return render(request, 'error/403.html')