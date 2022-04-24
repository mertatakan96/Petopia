from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home-page"),
    path('register-choose/', views.register_choose, name="register-choose"),
    path('register-petlover/', views.register_petlover, name="register-petlover"),
    path('register-business/', views.register_business, name="register-business"),
]