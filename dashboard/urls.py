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

    path('dashboard-delete-user/<str:pk>', views.admin_dashboard_delete_user, name="admin-dashboard-delete-user"),
    path('dashboard-delete-blog/<str:pk>', views.admin_dashboard_delete_blog, name="admin-dashboard-delete-blog"),
    path('dashboard-delete-forum/<str:pk>', views.admin_dashboard_delete_forum, name="admin-dashboard-delete-forum"),
    path('dashboard-delete-adopted/<str:pk>', views.admin_dashboard_delete_adopted, name="admin-dashboard-delete-adopted"),
    path('dashboard-delete-founded/<str:pk>', views.admin_dashboard_delete_founded, name="admin-dashboard-delete-founded"),
    path('dashboard-delete-lost/<str:pk>', views.admin_dashboard_delete_lost, name="admin-dashboard-delete-lost"),

    path('dashboard-close-adopted/<str:pk>', views.admin_dashboard_close_adopted, name="admin-dashboard-close-adopted"),
    path('dashboard-close-founded/<str:pk>', views.admin_dashboard_close_founded, name="admin-dashboard-close-founded"),
    path('dashboard-close-lost/<str:pk>', views.admin_dashboard_close_lost, name="admin-dashboard-close-lost"),



]
