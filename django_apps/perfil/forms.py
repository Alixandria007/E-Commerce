from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . import models

class PerfilForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
    class Meta:
        model = models.Perfil
        fields = ('__all__')
        exclude = 'usuario',

class UserForm(forms.ModelForm):
     
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha',
    )
     
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirmação senha'
    )

    def __init__(self, usuario = None ,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.usuario = usuario

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'email', 'password',

    def clean(self,*args,**kwargs):
        cleaned_data = self.cleaned_data

        usuario_data = cleaned_data['username']
        email_data = cleaned_data['email']
        password_data = cleaned_data['password']
        password2_data = cleaned_data['password2']


        usuario_db = User.objects.filter(username = usuario_data, email = email_data).first()
        
        if self.usuario:
            
            if usuario_db:
                if usuario_data != usuario_db.username:
                    self.add_error(
                        'username',
                        ValidationError('Usuario invalido.')
                    )

                if email_data != usuario_db.email:
                    self.add_error(
                        'emails',
                        ValidationError('Email Invalido.')
                    )

                if password_data:
                    if password_data != password2_data:
                        self.add_error(
                            'password',
                            ValidationError('As senhas não são compativeis.')
                        )

                    if len(password_data) < 6:
                        self.add_error(
                            'password',
                            ValidationError('A senha é muito curta.')
                        )
        else:

            if usuario_db:
                self.add_error(
                    'username',
                    ValidationError('Este usuario já existe.')
                )

            if password_data == '':
                self.add_error(
                    'password',
                    ValidationError('Senha requirida.')
                )

            if password2_data == '':
                self.add_error(
                    'password2',
                    ValidationError('Confirmação de senha requirida.')
                )

            if len(password_data) < 6:
                        self.add_error(
                            'password',
                            ValidationError('A senha é muito curta.')
                        )

            if password_data:
                    if password_data != password2_data:
                        self.add_error(
                            'password',
                            ValidationError('As senhas não são compativeis.')
                        )


        return super().clean()
        
        