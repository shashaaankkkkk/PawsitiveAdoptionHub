from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import CustomUser

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_parent_of_pet:
                # Redirect users with 'is_parent_of_pet' role to a specific page
                login(request, user)
                return redirect('parent_home')
            elif user.is_vet:
                # Redirect users with 'is_vet' role to a specific page
                login(request, user)
                return redirect('vet_home')
            elif user.is_admin:
                # Redirect users with 'is_admin' role to a specific page
                login(request, user)
                return redirect('admin_home')
            else:
                # Redirect other users to a default page
                login(request, user)
                return redirect('default_home')
    return render(request, 'login.html')
