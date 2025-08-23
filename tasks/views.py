from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
from tasks.models import Employee

# App Folder Templates
def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def static_test(request):
    context = {
        'name': 'Raisul Islam',
        'age': 24, 
        'hobbies': ['Programming', 'Music', 'Cricket']
    }
    return render(request, "static_test.html", context)

# django forms and model form
def submit_task(request):
    employees = Employee.objects.all()
    form = TaskForm(employees=employees)
    context = {"form": form}
    return render(request, "submit_form.html", context)