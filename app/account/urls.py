from django.urls import path
from . import views
urlpatterns = [
    path('pro/', views.account_pro),
    path('client/', views.account_client)
]
