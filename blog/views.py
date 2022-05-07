from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import BlogCreationForm, BlogCommentForm
from .models import Blog
from .utils import paginateBlogs, searchBlogs

def blog_page(request):
    profile = request.user
    form = BlogCreationForm()
    blogs = Blog.objects.all()

    blogs, search_query = searchBlogs(request)
    custom_range, blogs = paginateBlogs(request, blogs, 4)

    if request.method == 'POST':
        form = BlogCreationForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = profile
            blog.save()
            messages.success(request, 'Blog was created successfully!')
            return redirect('blog-page')

    context = {'form': form, 'profile': profile, 'blogs': blogs, 'custom_range': custom_range, 'search_query': search_query}
    return render(request, 'blog/blog.html', context)

def blog_detail(request, pk):
    profile = request.user
    blog = Blog.objects.get(id=pk)
    # limiting the latest post div and exclude that blog
    latest = blog.owner.blog_set.exclude(id=blog.id)[0:5]

    form = BlogCommentForm()

    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = profile
            comment.blog = blog
            comment.save()
            messages.success(request, 'Comment was created successfully!')
            return redirect('blog-detail', pk=blog.id)

    context = {'profile': profile, 'blog': blog, 'form': form, 'latest': latest}
    return render(request, 'blog/blog-detail.html', context)

def edit_blog(request):
    return render(request, 'blog/blog-edit.html')