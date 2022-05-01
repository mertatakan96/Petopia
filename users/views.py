from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import BusinessCreationForm, PetLoverUserCreationForm


def home_page(request):
    return render(request, 'users/homepage.html')

def loginPage(request):
    return render(request, 'users/login.html')

def register_choose(request):
    return render(request, 'users/register-choose.html')

def register_petlover(request):
    form = PetLoverUserCreationForm()
    context = {'formUser': form}
    return render(request, 'users/register-petlover.html', context)

def register_business(request):
    form = BusinessCreationForm()

    if request.method == 'POST':
        form = BusinessCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.user_type = 'business'
            user.save()

            login(request, user)
            print('User created')
            return redirect('home-page')
        else:
            print('Error')

    context = {'form': form}
    return render(request, 'users/register-business.html', context)

def petlover_profile(request):
    return render(request, 'users/petlover-profile.html')

def business_profile(request):
    return render(request, 'users/business-profile.html')

def testPage(request):
    form = PetLoverUserCreationForm()

    if request.method == 'POST':
        form = PetLoverUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.user_type = 'petlover'
            user.save()

            # login(request, user)
            print('User created')

            return redirect('home-page')
        else:
            print('Error')
            messages.error(request, messages.error)

    context = {'formUser': form}
    return render(request, 'users/test.html', context)