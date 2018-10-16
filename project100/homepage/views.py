from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'homepage/home.html')

def about(request):
    return render(request, 'homepage/about.html')

def contact(request):
    return render(request, 'homepage/contact.html')

def register(request):
    return render(request, 'homepage/register.html')

def login(request):
    return render(request, 'homepage/login.html') 