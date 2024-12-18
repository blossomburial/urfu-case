from .models import Jobs
from django import forms
from django.forms import ModelForm, TextInput, Select
from .models import UserProfile, Application

class JobsForm(ModelForm):
    class Meta:
        model = Jobs
        fields = ['title', 'desc', 'type_of_job', 'salary']

        widgets = {
            "title": TextInput(attrs={
                'class': '',
                'placeholder': 'название вакансии' 
            }),
            "desc": TextInput(attrs={
                'class': '',
                'placeholder': 'описание вакансии' 
            }),
            "type_of_job": Select(attrs={
                'class': '',
                'placeholder': 'тип вакансии' 
            }),
            "salary": TextInput(attrs={
                'class': '',
                'placeholder': 'заработная плата' 
            }),
        }

class JobSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="ключевые слова")
    type_of_job = forms.ChoiceField(
        choices=[('', 'все категории')] + list(Jobs.type_of_jobs), 
        required=False,
        label="категория"
    )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'birth_date', 'profile_picture', 'status']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter', 'resume'] 