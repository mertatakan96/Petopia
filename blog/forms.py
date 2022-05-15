from django import forms
from django.forms import ModelForm
from .models import Blog, BlogComment

class BlogCreationForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_image', 'title', 'post']

class BlogEditForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_image', 'title', 'post']

class BlogCommentForm(ModelForm):
    class Meta:
        model = BlogComment
        fields = ['body']