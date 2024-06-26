from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views import View

# Create your views here.


@login_required()
def home(request):
    return render(request, 'home.html')