from django.urls import path
from . import views
urlpatterns = [
    path('pro/', views.account_pro, name='account_pro'),
    path('client/', views.account_client, name='account_client'),
    path('services/', views.account_services, name='account_services'),
]
