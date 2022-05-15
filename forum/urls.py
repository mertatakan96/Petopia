from django.urls import path
from . import views

urlpatterns = [
    path('forums/', views.forum_page, name="forum-page"),
    path('forum/', views.forum_detail, name="forum-detail"),
]