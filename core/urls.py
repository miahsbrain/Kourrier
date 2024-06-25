from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.home, name='Home'),
    path('', include('social_django.urls', namespace='social')),
    path('courier/', views.courrier, name='Courier'),
    path('customer/', views.customer, name='Customer'),
    path('signin/', auth_view.LoginView.as_view(template_name='signin.html'), name='Signin'),
    path('signout/', auth_view.LogoutView.as_view(next_page='/'), name='Signout'),
    path('signup/', views.Signup.as_view(), name='Signup'),
]