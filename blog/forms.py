from .models import  Comment
from django import forms

from django.forms import Textarea

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
