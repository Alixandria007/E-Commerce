from typing import Any
from django import forms
from django.contrib.auth.models import User
from . import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = ('__all__')
        exclude = 'usuario',

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'email', 'password',

    def clean(self,*args,**kwargs):
        cleaned_data = self.cleaned_data
        return super().clean()
        ...