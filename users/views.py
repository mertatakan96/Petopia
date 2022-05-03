from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import BusinessCreationForm, PetLoverUserCreationForm, PetCreationForm, BusinessEditForm, PetLoverEditForm, PetEditForm
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
    pets = profile.pet_set.all()

    context = {'profile': profile, 'pets': pets}
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

@login_required(login_url='login')
def edit_profile(request):
    profile = request.user
    petlover_form = PetLoverEditForm(instance=profile)
    business_form = BusinessEditForm(instance=profile)

    if request.method == 'POST':
        form = PetLoverEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return  redirect('profile')

    if request.method == 'POST':
        form = BusinessEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return  redirect('profile')

    context = {'profile': profile, 'petlover_form': petlover_form, 'business_form':business_form}

    return render(request, 'users/edit-profile-form.html', context)

@login_required(login_url='login')
def add_pet(request):
    profile = request.user
    form = PetCreationForm()

    if request.method == 'POST':
        form = PetCreationForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = profile
            pet.save()
            return redirect('profile')

    context = {'form': form}

    return render(request, 'users/add-pet-form.html', context)

@login_required(login_url='login')
def edit_pet(request, pk):
    profile = request.user
    pet = profile.pet_set.get(id=pk)
    form = PetEditForm(instance=pet)

    if request.method == 'POST':
        form = PetEditForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}

    return render(request, 'users/edit-pet-form.html', context)

def forget_password(request):
    return render(request, 'users/forget-password-form.html')