from django.urls import path
from . import views

urlpatterns = [
    path('founded-announce/', views.founded_page, name="founded-announce"),
    path('adopt-announce/', views.adopt_page, name="adopt-announce"),
    path('lost-announce/', views.lost_page, name="lost-announce"),
]