from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_page, name="forum-page"),
    path('forum-detail/', views.forum_detail, name="forum-detail"),
]