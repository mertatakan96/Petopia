from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name="admin-dashboard"),

    path('dashboard-petlover/', views.admin_dashboard_petlover, name="admin-dashboard-petlover"),
    path('dashboard-business/', views.admin_dashboard_business, name="admin-dashboard-business"),
    path('dashboard-blogs/', views.admin_dashboard_blogs, name="admin-dashboard-blogs"),
    path('dashboard-forums/', views.admin_dashboard_forums, name="admin-dashboard-forums"),
    path('dashboard-adopted/', views.admin_dashboard_adopted, name="admin-dashboard-adopted"),
    path('dashboard-founded/', views.admin_dashboard_founded, name="admin-dashboard-founded"),
    path('dashboard-lost/', views.admin_dashboard_lost, name="admin-dashboard-lost"),

    path('dashboard-announce/', views.admin_dashboard_announce_list, name="admin-dashboard-announce")

]
