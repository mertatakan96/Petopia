from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import BusinessCreationForm, PetLoverUserCreationForm, PetCreationForm, BusinessEditForm, PetLoverEditForm, PetEditForm
from .models import User
from blog.models import Blog
from forum.models import Forum
from .utils import paginatePets, paginateBlogs, paginateForums


def home_page(request):
    profile = request.user
    blogs = Blog.objects.all()[0:3]
    forums = Forum.objects.all()[0:9]

    context = {'blogs': blogs, 'profile': profile, 'forums': forums}
    return render(request, 'users/homepage.html', context)

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
            return redirect(request.GET['next'] if 'next' in request.GET else 'home-page')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return redirect('home-page')

def register_choose(request):
    if request.user.is_authenticated:
        return redirect('home-page')

    return render(request, 'users/register-choose.html')

def register_petlover(request):

    if request.user.is_authenticated:
        return redirect('home-page')

    form = PetLoverUserCreationForm()

    if request.method == 'POST':
        form = PetLoverUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.user_type = 'petlover'
            user.save()

            login(request, user)
            # messages.success(request, 'Pet Lover Account successfully created')
            return redirect('home-page')
        else:
            password1 = form.data['password1']
            password2 = form.data['password2']
            email = form.data['email']
            username = form.data['username']
            for msg in form.errors.as_data():
                if msg == 'username':
                    messages.error(request, "Username already taken!")
                if msg == 'email':
                    messages.error(request, "Email already taken!")
                if msg == 'password2' and password1 == password2:
                    messages.error(request, "Password is not strong enough")
                elif msg == 'password2' and password1 != password2:
                    messages.error(request,
                                   "Passwords does not match")

    context = {'formUser': form}
    return render(request, 'users/register-petlover.html', context)

def register_business(request):

    if request.user.is_authenticated:
        return redirect('home-page')

    form = BusinessCreationForm()

    if request.method == 'POST':
        form = BusinessCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.user_type = 'business'
            user.save()

            login(request, user)
            # messages.success(request, 'Business Account successfully created')
            return redirect('home-page')
        else:
            password1 = form.data['password1']
            password2 = form.data['password2']
            email = form.data['email']
            username = form.data['username']
            for msg in form.errors.as_data():
                if msg == 'username':
                    messages.error(request, "Username already taken!")
                if msg == 'email':
                    messages.error(request, "Email already taken!")
                if msg == 'password2' and password1 == password2:
                    messages.error(request, "Password is not strong enough")
                elif msg == 'password2' and password1 != password2:
                    messages.error(request,
                                   "Passwords does not match")

    context = {'form': form}
    return render(request, 'users/register-business.html', context)

@login_required(login_url='login')
def user_profile(request):
    profile = request.user
    pets = profile.pet_set.all()
    blogs = profile.blog_set.all()
    forums = profile.forum_set.all()

    custom_range, pets = paginatePets(request, pets, 2)
    custom_range, blogs = paginateBlogs(request, blogs, 7)
    custom_range, forums = paginateBlogs(request, forums, 10)

    context = {'profile': profile, 'pets': pets, 'custom_range': custom_range, 'blogs': blogs, 'forums': forums}
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def edit_profile(request):
    profile = request.user
    petlover_form = PetLoverEditForm(instance=profile)
    business_form = BusinessEditForm(instance=profile)

    if request.method == 'POST':
        form = PetLoverEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'User was added edited')
            return redirect('profile')

    if request.method == 'POST':
        form = BusinessEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully edited')
            return redirect('profile')

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
            messages.success(request, 'Pet was added successfully!')
            return redirect('profile')

    context = {'form': form, 'profile': profile}

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
            messages.success(request, 'Pet was added edited!')
            return redirect('profile')

    context = {'form': form, 'profile': profile}

    return render(request, 'users/edit-pet-form.html', context)

def forget_password(request):
    return render(request, 'users/forget-password-form.html')

def admin_panel(request):
    return render(request, 'users/admin-panel.html')
