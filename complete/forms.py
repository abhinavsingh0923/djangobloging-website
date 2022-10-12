
from django import forms
from .models import *


class postfunction(forms.ModelForm):
    class Meta:
        model=Post
        fields=['author','title','content']
        widgets={
            'author':forms.TextInput(attrs={'class':'form-control', 'placeholder':"enter your name"}),
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':"enter your title"}),
            'content':forms.TextInput(attrs={'class':'form-control', 'placeholder':"write your content"}),
        }


