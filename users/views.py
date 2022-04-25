from django.shortcuts import render


def home_page(request):
    return render(request, 'users/homepage.html')

def loginPage(request):
    return render(request, 'users/login.html')

def register_choose(request):
    return render(request, 'users/register-choose.html')

def register_petlover(request):
    return render(request, 'users/register-petlover.html')

def register_business(request):
    return render(request, 'users/register-business.html')

def petlover_profile(request):
    return render(request, 'users/petlover-profile.html')

def business_profile(request):
    return render(request, 'users/business-profile.html')