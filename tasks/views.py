from django.shortcuts import render
from django.http import HttpResponse

# App Folder Templates
def manager_dashboard(request):
    return render(request, "dashboard.html")

def user_dashboard(request):
    return render(request, "user-dashboard.html")