from django.urls import path
from . import views

urlpatterns = [
    path('founded-announce/', views.founded_page, name="founded-announce"),
    path('adopt-announce/', views.adopt_page, name="adopt-announce"),
    path('lost-announce/', views.lost_page, name="lost-announce"),
    path('adopt-announce/<str:pk>', views.adopt_announce_page, name="adopt-announce-detail"),
    path('founded-announce/<str:pk>', views.founded_announce_page, name="founded-announce-detail"),
    path('lost-announce/<str:pk>', views.lost_announce_page, name="lost-announce-detail"),
]