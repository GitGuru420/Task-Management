from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
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
    form = TaskForm(employees=employees)
    
    # For POST
    if request.method == "POST":
        form = TaskForm(request.POST, employees=employees)
        if form.is_valid():
            data = form.cleaned_data
            title = data.get('title')
            descriptions = data.get('descriptions')
            due_date = data.get('due_date')
            employoee = data.get('employoee')
            print(employoee)
            
            task = Task.objects.create(title=title, descriptions=descriptions, due_date=due_date)
            
            # assigne employee to tasks
            for emp_id in employoee:
                employee = Employee.objects.get(id=emp_id)
                task.employoee.add(employee)
                
            return HttpResponse("Task Added Successfully")
    context = {"form": form}
    return render(request, "submit_form.html", context)