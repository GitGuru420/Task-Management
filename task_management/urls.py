from django.contrib import admin
from django.urls import path, include
from tasks.views import home_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home-view/', home_view),
    path('contact-view/', contact_view),
    path('tasks/', include('tasks.urls')),
]
