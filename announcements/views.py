from django.shortcuts import render, redirect
from .forms import FoundedPetCreationForm, AdoptPetCreationForm, LostPetCreationForm,\
    FoundedCommentForm, AdoptCommentForm, LostCommentForm
from .models import AdoptPet, FoundedPet, LostPet
from .utils import paginateAdopts, paginateLosts, paginateFoundeds


def adopt_page(request):
    profile = request.user
    form = AdoptPetCreationForm()
    adopt = AdoptPet.objects.all()

    custom_range, adopt = paginateAdopts(request, adopt, 6)

    if request.method == 'POST':
        form = AdoptPetCreationForm(request.POST, request.FILES)
        if form.is_valid():
            adopt = form.save(commit=False)
            adopt.save()
            return redirect('adopt-announce')

    context = {'form': form, 'adopt': adopt, 'profile': profile, 'custom_range': custom_range}
    return render(request, 'announcements/adopted-announce.html', context)

def founded_page(request):
    profile = request.user
    form = FoundedPetCreationForm()
    founded = FoundedPet.objects.all()

    custom_range, founded = paginateFoundeds(request, founded, 6)

    if request.method == 'POST':
        form = FoundedPetCreationForm(request.POST, request.FILES)
        if form.is_valid():
            founded = form.save(commit=False)
            founded.save()
            return redirect('founded-announce')

    context = {'form': form, 'founded': founded, 'profile': profile, 'custom_range': custom_range}
    return render(request, 'announcements/founded-announce.html', context)

def lost_page(request):
    profile = request.user
    form = LostPetCreationForm()
    lost = LostPet.objects.all()

    custom_range, lost = paginateLosts(request, lost, 6)

    if request.method == 'POST':
        form = LostPetCreationForm(request.POST, request.FILES)
        if form.is_valid():
            lost = form.save(commit=False)
            lost.save()
            return redirect('lost-announce')

    context = {'form': form, 'lost': lost, 'profile': profile, 'custom_range': custom_range}
    return render(request, 'announcements/lost-announce.html', context)

def adopt_announce_page(request, pk):
    profile = request.user
    adopt = AdoptPet.objects.get(id=pk)

    form = AdoptCommentForm()

    if request.method == 'POST':
        form = AdoptCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = profile
            comment.announce = adopt
            comment.save()
            return redirect('adopt-announce-detail', pk=adopt.id)

    context = {'adopt': adopt, 'profile': profile, 'form': form}
    return render(request, 'announcements/adopt-detail.html', context)

def founded_announce_page(request, pk):
    profile = request.user
    found = FoundedPet.objects.get(id=pk)

    form = FoundedCommentForm()

    if request.method == 'POST':
        form = FoundedCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = profile
            comment.announce = found
            comment.save()
            return redirect('founded-announce-detail', pk=found.id)

    context = {'found': found, 'profile': profile, 'form': form}
    return render(request, 'announcements/founded-detail.html', context)

def lost_announce_page(request, pk):
    profile = request.user
    lost = LostPet.objects.get(id=pk)

    form = LostCommentForm()

    if request.method == 'POST':
        form = LostCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = profile
            comment.announce = lost
            comment.save()
            return redirect('lost-announce-detail', pk=lost.id)

    context = {'lost': lost, 'profile': profile, 'form': form}
    return render(request, 'announcements/lost-detail.html', context)
