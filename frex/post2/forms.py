from django import forms
from .models import Coment2

class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment2
        fields = ['coment']
