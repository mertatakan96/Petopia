from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import BusinessCreationForm, PetLoverUserCreationForm
from .models import User


def home_page(request):
    return render(request, 'users/homepage.html')

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home-page')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return redirect('home-page')

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

@login_required(login_url='login')
def user_profile(request):
    profile = request.user

    context = {'profile': profile}
    return render(request, 'users/profile.html', context)


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

def edit_profile(request):
    return render(request, 'users/edit-profile-form.html')

def add_pet(request):
    return render(request, 'users/edit-profile-form.html')

def edit_pet(request):
    return render(request, 'users/edit-profile-form.html')