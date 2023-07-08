from .models import *
from django.forms import ModelForm, TextInput, Textarea
from django import forms


            
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
                'name': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': "Имя"
                }),
                'body': Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': "Текст"
                }),}