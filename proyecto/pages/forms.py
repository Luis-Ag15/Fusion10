from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        Widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'title':'',
        }
        