from django.urls import path
from . import views

urlpatterns = [
    path('forums/', views.forum_page, name="forum-page"),
    path('forum/<str:pk>', views.forum_detail, name="forum-detail"),
    path('forum-edit/<str:pk>', views.forum_edit, name="forum-edit"),
]