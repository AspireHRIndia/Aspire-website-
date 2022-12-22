from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def adminHome(request):
    messages.success(request, "Welcome to admin")
    return render(request, 'admin_home.html')

