from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'login/login.html')

def home_view(request):
    return render(request, 'home/index.html')

def register_view(request):
    return render(request, 'register/register.html')