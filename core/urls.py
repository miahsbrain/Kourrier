from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view
from core.customer import views as customer_views
from core.courier import views as courier_views

customer_urlpatterns = [
    path('', customer_views.home, name='home'),
    path('profile/', customer_views.profile, name='profile'),
]

courier_urlpatterns = [
    path('', courier_views.home, name='home'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('social_django.urls', namespace='social')),


    path('signin/', auth_view.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('signout/', auth_view.LogoutView.as_view(next_page='/'), name='signout'),
    path('signup/', views.Signup.as_view(), name='signup'),


    path('customer/', include((customer_urlpatterns, 'customer'))),
    path('courier/', include((courier_urlpatterns, 'courier'))),
]