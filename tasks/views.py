from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task

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
    form = TaskModelForm()
    
    # For POST
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            """ For Model Form Data"""
            form.save()
            
            return render(request, 'submit_form.html', {"form": form, "message": "Task Added Successfully"})
    context = {"form": form}
    return render(request, "submit_form.html", context)