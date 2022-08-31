from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, auth
from .models import Profile
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Użytkownik o takiej nazwie istnieje')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,
                                                password=password2)
                user.save()

                #Log user in and redirect to settings page

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,
                                                     id_user=user_model.id)
                new_profile.save()

                return redirect('signin')
        else:
            messages.info(request, 'Hasło nie pasuje')
            return redirect('signup')
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = auth.authenticate(username=username, password=password1)

        if user is not None:
            auth.login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'Użytkownik lub hasło nie pasuje')
            return redirect('signin')

    return render(request, 'signin.html')