from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_page, name="blog-page"),
    path('blog-detail/<str:pk>', views.blog_detail, name="blog-detail"),
    path('edit-blog/', views.edit_blog, name="edit-blog"),
]