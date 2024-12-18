from .models import Jobs, Category
from django import forms
from django.forms import ModelForm, TextInput

class JobsForm(ModelForm):
    class Meta:
        model = Jobs
        fields = ['title', 'desc', 'type_of_job']

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
        }

class JobSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="Ключевые слова")
    type_of_job = forms.ChoiceField(
        choices=[('', 'Все категории')] + list(Jobs.TYPE_OF_JOB_CHOICES), 
        required=False,
        label="Категория"
    )