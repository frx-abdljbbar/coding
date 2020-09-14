from django import forms
from .models import Coment3

class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment3
        fields = ['coment']
