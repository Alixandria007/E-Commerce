from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import copy
from . import models

# Create your views here.

def criar_perfil(request):

    carrinho = copy.deepcopy(request.session.get('carrinho', {}))
    
    if request.user.is_authenticated:
        perfil = models.Perfil.objects.filter(
                usuario=request.user
            ).first()
        

        context = {
                'userform': forms.AtualizarForm(
                    data = request.POST or None,
                    usuario=request.user,
                    instance = request.user
                ),
                'perfilform': forms.PerfilForm(
                    data = request.POST or None,
                    instance = perfil
                ),
                'titulo': 'Atualizar',
            }
        
    else:
        context = {
                'userform': forms.UserForm(
                    data = request.POST or None,
                    usuario=request.user
                ),
                'perfilform': forms.PerfilForm(
                    data = request.POST or None
                ),
                'titulo': 'Login',
            }
        
    userform = context['userform']
    perfilform = context['perfilform']

    if request.method == 'POST':
        
        if not userform.is_valid() or not perfilform.is_valid():
            messages.error(
                request,
                'Existem erros no formulário de cadastro. Verifique se todos '
                'os campos foram preenchidos corretamente.'
            )
            return render(request,'loja/pages/criar_perfil.html',context)
        
        first_name = userform.cleaned_data.get('first_name')
        last_name = userform.cleaned_data.get('last_name')
        username = userform.cleaned_data.get('username')
        email = userform.cleaned_data.get('email')
        password = userform.cleaned_data.get('password')

        if request.user.is_authenticated:
            usuario = get_object_or_404(User, username = request.user.username)

            usuario.username = username
            usuario.email = email
            if password:
                usuario.set_password(password)
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()

            if not perfil:
                perfilform.cleaned_data['usuario'] = usuario
                perfil = models.Perfil(**perfilform.cleaned_data)
                perfil.save()
            else:
                perfil = perfilform.save(commit=False)
                perfil.usuario = usuario
                perfil.save()


        else:
            usuario = userform.save(commit = False)
            usuario.set_password(password)
            usuario.save()

            perfil = perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()
            
            messages.success(
            request,
            'Seu cadastro foi criado ou atualizado com sucesso.'
            )

            if password:
                autenticar = authenticate(
                    request,
                    username = usuario,
                    password = password
                )

            if autenticar:
                login(request, user = usuario)
            else:
                pass

        

        messages.success(
            request,
            'Você fez login e pode concluir sua compra.'
        )

        return redirect('produto:carrinho')
    
    if request.user.is_authenticated:
        return render(request,'loja/pages/atualizar.html',context)
    else:
        return render(request,'loja/pages/criar_perfil.html',context)

def update(request):
    ...

def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(
                request,
                'Usuario ou senha invalidos!'
            )

            return redirect('perfil:criar_perfil')

        usuario = authenticate(request, username = username, password = password)

        if not usuario:
            messages.error(
                request,
                'Usuario não existe!'
            )

            return redirect('perfil:criar_perfil')
        
        login(request, user = usuario)

        messages.success(
            request,
            'Você fez login no sistema e pode concluir sua compra.'
        )

        return redirect('produto:index')

def logout_(request):
    carrinho = copy.deepcopy(request.session.get('carrinho'))

    logout(request)

    request.session['carrinho'] = carrinho
    request.session.save()

    return redirect('produto:index')