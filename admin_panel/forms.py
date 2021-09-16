from django import forms
from django.forms import fields
from school_app.models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','post','image',]