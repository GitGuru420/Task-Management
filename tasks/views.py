from django.shortcuts import render
from django.http import HttpResponse

# App Folder Templates
def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def static_test(request):
    return render(request, "static_test.html")