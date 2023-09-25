from .models import Tasks
from django.forms import ModelForm, TextInput, NumberInput


class TasksForm(ModelForm):   #форма добавление/изменения в БД
    class Meta:
        model = Tasks
        fields = ['number', 'title', 'text']

        widgets = {
            'number': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер задачи'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название задачи'
            }),
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание задачи'
            }),
        }
