from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ForumCreationForm, ForumEditForm, ForumCommentForm
from .models import Forum
from .utils import paginateForums, searchForums
from django.contrib.auth.decorators import login_required

def forum_page(request):
    profile = request.user
    form = ForumCreationForm()
    forums = Forum.objects.all()

    forums, search_query = searchForums(request)
    custom_range, forums = paginateForums(request, forums, 12)

    if request.method == 'POST':
        form = ForumCreationForm(request.POST, request.FILES)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.owner = profile
            forum.save()
            messages.success(request, 'Forum was created successfully!')
            return redirect('forum-page')

    context = {'form': form, 'profile': profile, 'forums': forums, 'custom_range': custom_range, 'search_query': search_query}
    return render(request, 'forum/forum.html', context)

def forum_detail(request, pk):
    profile = request.user
    forum = Forum.objects.get(id=pk)
    # limiting the latest post div and exclude that blog
    latest = None
    if(forum.owner != None):
        latest = forum.owner.forum_set.exclude(id=forum.id)[0:5]

    form = ForumCommentForm()

    if request.method == 'POST':
        form = ForumCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = profile
            comment.forum = forum
            comment.save()
            messages.success(request, 'Comment was created successfully!')
            return redirect('forum-detail', pk=forum.id)

    context = {'profile': profile, 'forum': forum, 'latest': latest, 'form': form}
    return render(request, 'forum/forum-detail.html', context)

@login_required(login_url='login')
def forum_edit(request, pk):
    profile = request.user
    forum = Forum.objects.get(id=pk)
    form = ForumEditForm(instance=forum)

    if request.method == 'POST':
        form = ForumEditForm(request.POST, request.FILES, instance=forum)
        if form.is_valid():
            form.save()
            return redirect('forum-detail', pk=forum.id)

    context = {'form': form, 'forum': forum}
    return render(request, 'forum/forum-edit.html', context)
