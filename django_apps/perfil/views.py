from django.shortcuts import render
from . import forms
from django.contrib import messages

# Create your views here.

def criar_perfil(request):

    if request.method == 'POST':
        if not self.userform.is_valid() or not self.perfilform.is_valid():
            messages.error(
                self.request,
                'Existem erros no formulário de cadastro. Verifique se todos '
                'os campos foram preenchidos corretamente.'
            )

    context = {
        'userform': forms.UserForm(
            data = request.POST or None,
            usuario=request.user
        ),
        'perfilform': forms.PerfilForm(
            data = request.POST or None
        ),
    }
    return render(request,'loja/pages/criar_perfil.html',context)

def update(request):
    ...

def login(request):
    ...

def logout(request):
    ...