from django.urls import path, include
from . import views
urlpatterns = [
    path('pro/', views.account_pro, name='account_pro'),
    path('client/', views.account_client, name='account_client'),
    path('services/', views.account_services, name='account_services'),
    path('practiens/', views.show_all_practicien, name='show_all_practicien'),
    path('localisation/', views.account_localisation, name='account_localisation'),
    path('', include('booking.urls'))
]
