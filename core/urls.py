from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('courrier/', views.courrier, name='Courrier'),
    path('customer/', views.customer, name='Customer'),
]