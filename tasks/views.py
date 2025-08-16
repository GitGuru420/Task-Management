from django.shortcuts import render
from django.http import HttpResponse

# Home View
def home_view(request):
    return HttpResponse("<h1>Welcome to the Task Management System</h1>")

# Contact View
def contact_view(request):
    return HttpResponse("<h1>This is the Contact Page. Reach us at contact@taskmanagement.com</h1>")