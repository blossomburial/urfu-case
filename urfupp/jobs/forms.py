from .models import Jobs
from django import forms
from django.forms import ModelForm, TextInput, Form

class JobsForm(ModelForm):
    class Meta:
        model = Jobs
        fields = ['title', 'desc', 'type_of_job', 'busyness']

        widgets = {
            "title": TextInput(attrs={
                'class': '',
                'placeholder': 'название вакансии' 
            }),
            "desc": TextInput(attrs={
                'class': '',
                'placeholder': 'описание вакансии' 
            }),
            "type_of_job": TextInput(attrs={
                'class': '',
                'placeholder': 'тип вакансии' 
            }),
            "busyness": TextInput(attrs={
                'class': '',
                'placeholder': 'занятость' 
            }),
        }

class SearchForm(Form):
    query = forms.CharField(max_length=100, label="Поиск", required=False)
