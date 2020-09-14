from django import forms
from .models import Coment1

class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment1
        fields = ['coment']
