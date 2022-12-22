from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username=request.POST['email-username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Logged in Successfully!")
            return redirect('home')
        else:
            messages.error(request, "Some error occured while logging in. Please try again...")
            return redirect('login')

    context = {
       
    }

    return render(request, 'login.html', context)


def user_logout(request):
    auth_logout(request)
    messages.info(request, "Logged out successfully!")

    return redirect('home')