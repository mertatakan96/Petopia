from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import User, Pet
from forum.models import Forum
from blog.models import Blog
from announcements.models import AdoptPet, FoundedPet, LostPet
from announcements.forms import FoundedPetEditForm, AdoptPetEditForm, LostPetEditForm
from .utils import paginateBlogs, paginateForums, paginatePetlovers, paginateBusiness,\
    paginateAdopted, paginateFounded, paginateLost

@login_required(login_url='login')
def admin_dashboard(request):
    profile = request.user
    pet_lover_account_count = User.objects.all().filter(user_type='petlover').count()
    business_account_count = User.objects.all().filter(user_type='business').count()
    pet_count = Pet.objects.all().count()
    forum_count = Forum.objects.all().count()
    blog_count = Blog.objects.all().count()
    adopt_count = AdoptPet.objects.all().count()
    founded_count = FoundedPet.objects.all().count()
    lost_count = LostPet.objects.all().count()

    context = {'pl_count': pet_lover_account_count, 'busi_count': business_account_count,
               'forum_count': forum_count, 'blog_count': blog_count, 'adopt_count': adopt_count,
               'founded_count': founded_count, 'lost_count':lost_count, 'pet_count': pet_count, 'profile': profile}
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
def admin_dashboard_petlover(request):
    profile = request.user
    pet_lover_accounts = User.objects.all().filter(user_type='petlover')

    custom_range, pet_lover_accounts = paginatePetlovers(request, pet_lover_accounts, 13)

    context= {'petlovers': pet_lover_accounts, 'profile': profile, 'custom_range': custom_range}
    return render(request, 'dashboard/dashboard-petlover.html', context)

@login_required(login_url='login')
def admin_dashboard_business(request):
    profile = request.user
    business_accounts = User.objects.all().filter(user_type='business')

    custom_range, business_accounts = paginateBusiness(request, business_accounts, 13)

    context = {'business': business_accounts, 'profile': profile, 'custom_range': custom_range}
    return render(request, 'dashboard/dashboard-business.html', context)

@login_required(login_url='login')
def admin_dashboard_blogs(request):
    profile = request.user
    blogs = Blog.objects.all()

    custom_range, blogs = paginateBlogs(request, blogs, 13)

    context = {'blogs': blogs, 'profile': profile, 'custom_range': custom_range}
    return render(request, 'dashboard/dashboard-blogs.html', context)

@login_required(login_url='login')
def admin_dashboard_forums(request):
    profile = request.user
    forums = Forum.objects.all()

    custom_range, forums = paginateBlogs(request, forums, 13)

    context = {'forums': forums, 'profile': profile, 'custom_range': custom_range}
    return render(request, 'dashboard/dashboard-forums.html', context)

@login_required(login_url='login')
def admin_dashboard_adopted(request):
    profile = request.user
    adopted = AdoptPet.objects.all()

    custom_range, adopted = paginateBlogs(request, adopted, 13)

    context = {'adopted': adopted, 'profile': profile, 'custom_range': custom_range}
    return render(request, 'dashboard/dashboard-adopted.html', context)

@login_required(login_url='login')
def admin_dashboard_founded(request):
    profile = request.user
    founded = FoundedPet.objects.all()

    custom_range, founded = paginateBlogs(request, founded, 13)

    context = {'founded': founded, 'profile': profile, 'custom_range': custom_range}
    return render(request, 'dashboard/dashboard-founded.html', context)

@login_required(login_url='login')
def admin_dashboard_lost(request):
    profile = request.user
    lost = LostPet.objects.all()

    custom_range, lost = paginateBlogs(request, lost, 13)

    context = {'lost': lost, 'profile': profile, 'custom_range': custom_range}
    return render(request, 'dashboard/dashboard-lost.html', context)

@login_required(login_url='login')
def admin_dashboard_delete_user(request, pk):
    profile = request.user
    user = User.objects.get(user_id=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('admin-dashboard')

    context = {'profile': profile, 'object': user}
    return render(request, 'dashboard/delete-form.html', context)

@login_required(login_url='login')
def admin_dashboard_delete_forum(request, pk):
    profile = request.user
    forum = Forum.objects.get(id=pk)

    if request.method == 'POST':
        forum.delete()
        return redirect('admin-dashboard')

    context = {'profile': profile, 'object': forum}
    return render(request, 'dashboard/delete-form.html', context)

@login_required(login_url='login')
def admin_dashboard_delete_blog(request, pk):
    profile = request.user
    blog = Blog.objects.get(id=pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('admin-dashboard')

    context = {'profile': profile, 'object': blog}
    return render(request, 'dashboard/delete-form.html', context)

@login_required(login_url='login')
def admin_dashboard_delete_adopted(request, pk):
    profile = request.user
    adopted = AdoptPet.objects.get(id=pk)

    if request.method == 'POST':
        adopted.delete()
        return redirect('admin-dashboard')

    context = {'profile': profile, 'object': adopted}
    return render(request, 'dashboard/delete-form.html', context)

@login_required(login_url='login')
def admin_dashboard_delete_founded(request, pk):
    profile = request.user
    founded = FoundedPet.objects.get(id=pk)

    if request.method == 'POST':
        founded.delete()
        return redirect('admin-dashboard')

    context = {'profile': profile, 'object': founded}
    return render(request, 'dashboard/delete-form.html', context)

@login_required(login_url='login')
def admin_dashboard_delete_lost(request, pk):
    profile = request.user
    lost = LostPet.objects.get(id=pk)

    if request.method == 'POST':
        lost.delete()
        return redirect('admin-dashboard')

    context = {'profile': profile, 'object': lost}
    return render(request, 'dashboard/delete-form.html', context)

@login_required(login_url='login')
def admin_dashboard_close_adopted(request, pk):
    profile = request.user
    adopted = AdoptPet.objects.get(id=pk)
    form = AdoptPetEditForm(instance=adopted)

    if request.method == 'POST':
        form = AdoptPetEditForm(request.POST, instance=adopted)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')

    context = {'profile': profile, 'object': adopted, 'form':form}
    return render(request, 'dashboard/status-form.html', context)

@login_required(login_url='login')
def admin_dashboard_close_founded(request, pk):
    profile = request.user
    founded = FoundedPet.objects.get(id=pk)
    form = FoundedPetEditForm(instance=founded)

    if request.method == 'POST':
        form = AdoptPetEditForm(request.POST, instance=founded)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')

    context = {'profile': profile, 'object': founded, 'form': form}
    return render(request, 'dashboard/status-form.html', context)

@login_required(login_url='login')
def admin_dashboard_close_lost(request, pk):
    profile = request.user
    lost = LostPet.objects.get(id=pk)
    form = LostPetEditForm(instance=lost)

    if request.method == 'POST':
        form = LostPetEditForm(request.POST, instance=lost)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')

    context = {'profile': profile, 'object': lost, 'form': form}
    return render(request, 'dashboard/status-form.html', context)

