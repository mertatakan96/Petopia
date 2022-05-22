from django.shortcuts import render, redirect
from .forms import FoundedPetCreationForm, AdoptPetCreationForm, LostPetCreationForm


def adopt_page(request):
    form = AdoptPetCreationForm()

    if request.method == 'POST':
        form = AdoptPetCreationForm(request.POST, request.FILES)
        if form.is_valid():
            adopt = form.save(commit=False)
            adopt.save()
            return redirect('adopt-announce')

    context = {'form': form}
    return render(request, 'announcements/adopted-announce.html', context)

def founded_page(request):
    form = FoundedPetCreationForm()

    if request.method == 'POST':
        form = FoundedPetCreationForm(request.POST, request.FILES)
        if form.is_valid():
            founded = form.save(commit=False)
            founded.save()
            return redirect('founded-announce')

    context = {'form': form}
    return render(request, 'announcements/founded-announce.html', context)

def lost_page(request):
    form = LostPetCreationForm()

    if request.method == 'POST':
        form = LostPetCreationForm(request.POST, request.FILES)
        if form.is_valid():
            lost = form.save(commit=False)
            lost.save()
            return redirect('founded-announce')

    context = {'form': form}
    return render(request, 'announcements/lost-announce.html', context)

def announce_page(request):
    return render(request, 'announcements/announce-detail.html')
