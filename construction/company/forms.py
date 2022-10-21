from django import forms
from django.forms import ModelForm
from .models import Applicants


class Applicantsform(ModelForm):
    class Meta:
       
        model= Applicants
        fields= ('first_name', 'last_name', 'country','nationality','phone','email','role_of_experience')

        widgets={
            'first-name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'nationality':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'role_of_experience':forms.TextInput(attrs={'class':'form-control'}),

        }