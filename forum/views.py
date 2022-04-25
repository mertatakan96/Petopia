from django.shortcuts import render

def forum_page(request):
    return render(request, 'forum/forum.html')

def forum_detail(request):
    return render(request, 'forum/forum-detail.html')
