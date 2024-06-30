from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class SignForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email', 'password1', 'password2')

        labels = {
            'username':'',
            'first_name':'',
            'last_name':'',
            'email':'',
            'password1':'',
            'password2':'',
        }

class OrphanForm(ModelForm):
    class Meta:
        model = Orphan

        fields = ('name','age','birthdate','details','photo')

        labels = {
            'name':'',
            'age':'',
            'birthdate':'',
            'details':'',
            'photo':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder':'Age','class':'form-control'}),
            'birthdate': forms.DateInput(attrs={'placeholder':'Birthdate','class':'form-control'}),
            'details': forms.TextInput(attrs={'placeholder':'Details','class':'form-control'}),
        }

class GuardianForm(ModelForm):
    class Meta:
        model = Guardian

        fields = ('name','email','address','phone')

        labels = {
            'name':'',
            'email':'',
            'address':'',
            'phone':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}),
            'address': forms.TextInput(attrs={'placeholder':'Address','class':'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder':'Phone','class':'form-control'}),
        }