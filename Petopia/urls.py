from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('forum/', include('forum.urls')),
    path('blog/', include('blog.urls')),
    path('', include('announcements.urls')),
]
