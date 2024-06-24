from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def customer(request):
    return render(request, 'customer.html')

def courrier(request):
    return render(request, 'courrier.html')