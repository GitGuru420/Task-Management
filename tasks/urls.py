from django.urls import path
from tasks.views import about_view, services_view

urlpatterns = [
    path('about-view/', about_view),
    path('service-view/', services_view),
]
