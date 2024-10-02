from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'completed'] 
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border-gray-300 p-2 rounded w-full',
                'placeholder': 'Task title...',
            }),
            'description': forms.Textarea(attrs={
                'class': 'border-gray-300 p-2 rounded w-full',
                'placeholder': 'Task description...',
                'rows': 4,
            }),
        }
        