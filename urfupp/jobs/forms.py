from .models import Jobs
from django.forms import ModelForm, TextInput

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