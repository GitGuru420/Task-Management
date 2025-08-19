from django.shortcuts import render
from django.http import HttpResponse

# Root Folder Templates
def home(request):
    return render(request, "home.html")