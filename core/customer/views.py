from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views import View
from . import forms
from django.contrib.auth.models import User

# Create your views here.


@login_required()
def home(request):
    return redirect(reverse('customer:profile'))

@login_required(login_url='/signin/?next=/customer')
def profile(request):

    user_form = forms.BasicUserForm(instance=request.user)
    customer_form = forms.BasicCustomerForm(instance=request.user.customer)

    if request.method == 'POST':
        print(request.POST)
        user_form = forms.BasicUserForm(data=request.POST, instance=request.user)
        customer_form = forms.BasicCustomerForm(data=request.POST, files=request.FILES, instance=request.user.customer)
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            return redirect(reverse('customer:profile'))

    return render(request, 'customer/profile.html', {'user_form': user_form, 'customer_form': customer_form})