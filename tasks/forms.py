from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=100, label="Task Title")
    descriptions = forms.CharField(widget=forms.Textarea, label="Task Description")
    due_date = forms.DateField(widget=forms.SelectDateWidget, label="Due Date")
    employoee = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[], label="Assigned To")
    
    def __init__(self, *args, **kwargs):
        employees = kwargs.pop("employees", [])
        super().__init__(*args, **kwargs)
        self.fields['employoee'].choices = [(emp.id, emp.name) for emp in employees]