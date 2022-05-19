from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home-page"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('register-choose/', views.register_choose, name="register-choose"),
    path('register-petlover/', views.register_petlover, name="register-petlover"),
    path('register-business/', views.register_business, name="register-business"),

    path('profile/', views.user_profile, name="profile"),
    path('edit-profile/', views.edit_profile, name="edit-profile"),
    path('add-pet/', views.add_pet, name="add-pet"),
    path('edit-pet/<str:pk>/', views.edit_pet, name="edit-pet"),

    path('forget-password', views.forget_password, name="forget-password"),

    path('admin-panel/', views.admin_panel, name="admin-panel")

]