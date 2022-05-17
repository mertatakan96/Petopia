from django.shortcuts import render

# Create your views here.

def adopt_page(request):
    return render(request, 'announcements/adopted-announce.html')

def founded_page(request):
    return render(request, 'announcements/founded-announce.html')

def lost_page(request):
    return render(request, 'announcements/lost-announce.html')

def announce_page(request):
    return render(request, 'announcements/announce-detail.html')
