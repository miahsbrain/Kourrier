from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required()
def customer(request):
    return render(request, 'customer.html')

@login_required()
def courrier(request):
    return render(request, 'courier.html')

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')