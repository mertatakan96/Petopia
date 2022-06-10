from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_page, name="home-page"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('register-choose/', views.register_choose, name="register-choose"),
    path('register-petlover/', views.register_petlover, name="register-petlover"),
    path('register-business/', views.register_business, name="register-business"),

    path('profile/', views.user_profile, name="profile"),
    path('profiles/<str:pk>', views.user_profiles, name="profiles"),

    path('edit-profile/', views.edit_profile, name="edit-profile"),
    path('add-pet/', views.add_pet, name="add-pet"),
    path('edit-pet/<str:pk>/', views.edit_pet, name="edit-pet"),

    path('delete-forum/<str:pk>', views.delete_forum, name="delete-forum"),
    path('delete-pet/<str:pk>', views.delete_pet, name="delete-pet"),
    path('delete-blog/<str:pk>', views.delete_blog, name="delete-blog"),

    path('password_change/', views.PasswordChangeView.as_view(template_name="users/change_password.html"), name="password_change"),
    path('password_success/', views.password_success, name="password_success"),


]