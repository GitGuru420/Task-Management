from django import forms
from tasks.models import Task
# Django Form
class TaskForm(forms.Form):
    title = forms.CharField(max_length=100, label="Task Title")
    descriptions = forms.CharField(widget=forms.Textarea, label="Task Description")
    due_date = forms.DateField(widget=forms.SelectDateWidget, label="Due Date")
    employoee = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[], label="Assigned To")
    
    def __init__(self, *args, **kwargs):
        employees = kwargs.pop("employees", [])
        super().__init__(*args, **kwargs)
        self.fields['employoee'].choices = [(emp.id, emp.name) for emp in employees]
        
# Django Model Form
class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'descriptions', 'due_date', 'employoee']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500",
                'placeholder': "Enter a descriptive task title"
            }),
            'descriptions': forms.Textarea(attrs={
                'class': "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm resize-none focus:outline-none focus:border-rose-500 focus:ring-rose-500",
                'placeholder': "Provide detailed task information",
                'rows': 5,
            }),
            'due_date': forms.SelectDateWidget(attrs={
                'class': "border-2 border-gray-300 p-2 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
            }),
            'employoee': forms.CheckboxSelectMultiple(attrs={
                'class': "space-y-2"
            })
        }