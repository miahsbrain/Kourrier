from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views import View
from . import forms
from django.http import HttpResponseRedirect

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
        form = forms.SignUpForm()
        return render(request, 'signup.html', {'form': form})
    
    def post(self, request):
        form = forms.SignUpForm(request.POST)
        print(request)
        if form.is_valid():
            email = form.cleaned_data['email'].lower()

            user = form.save(commit=False)
            user.username = email
            user.save()

            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'signup.html', {'form': form})