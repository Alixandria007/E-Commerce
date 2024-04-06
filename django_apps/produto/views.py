from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . import models
from django_apps.perfil.models import Perfil
# Create your views here.

def index(request):
    produtos = models.Produto.objects.all().order_by('-pk')

    paginator = Paginator(produtos,6)
    page_number = request.GET.get('page',None)
    page_obj = paginator.get_page(page_number)

    context = {
        'titulo': 'Home',
        'page_obj' : page_obj,
    }


    return render(request,'loja/pages/index.html', context)

def detalhes(request, slug):
    produto = models.Produto.objects.filter(slug = slug).first()

    context = {
        'prod' : produto,
    }

    return render(request,'loja/pages/detail.html', context)


@login_required(login_url='perfil:criar_perfil')
def adicionar_carrinho(request):
    produto_id = request.GET.get('id', None)

    if not produto_id:
        messages.error(
            request,
            'O produto não existe'
        )
        return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))


    produto = get_object_or_404(models.Produto, id = produto_id)

    produto_estoque = produto.estoque
    produto_nome = produto.nome
    preco_unico = produto.preco_marketing
    preco_unico_promo = produto.preco_marketing_promocional
    quantidade = int(request.GET.get('quantidade', 1))
    slug = produto.slug
    imagem = produto.imagem

    if imagem:
        imagem = imagem.name
    else:
        imagem = ''


    if produto_estoque < 1:
        messages.error(
            request,
            'Não há estoque o suficiente'
        )
        return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))
    
    user_id = str(request.user.id)

    if not request.session.get('carrinho'):
        request.session['carrinho'] = {}
        request.session.save()
    
    carrinho_ = request.session.get('carrinho')
    if user_id not in carrinho_:
        carrinho_[user_id] = {}
        request.session.save()

    carrinho = carrinho_[user_id]


    if produto_id in carrinho:
        quantidade_carrinho = carrinho[produto_id]['quantidade']
        quantidade_carrinho += quantidade

        if produto_estoque < quantidade_carrinho:
            messages.warning(
                request,
                f'Estoque insuficiente para {quantidade_carrinho} no {produto_nome}, Adicionamos {produto_estoque} ao Carrinho' 
            )
            quantidade_carrinho = produto_estoque

        carrinho[produto_id]['quantidade'] = quantidade_carrinho 
        carrinho[produto_id]['total'] = preco_unico * quantidade_carrinho
        if preco_unico_promo:
            carrinho[produto_id]['total_promo'] = preco_unico_promo * quantidade_carrinho

    else:
        if not preco_unico_promo:
            preco_unico_promo = 0


        carrinho[produto_id] = {
            'id': produto_id,
            'nome': produto_nome,
            'preco': preco_unico,
            'preco_promo': preco_unico_promo,
            'total': preco_unico * quantidade,
            'total_promo': preco_unico_promo * quantidade,
            'quantidade' : quantidade,
            'slug' : slug,
            'imagem' : imagem
        }

        request.session.save()
        
        messages.success(
                request,
                f'Adicionamos {quantidade}x {produto_nome} ao seu carrinho, temos no total agora {carrinho[produto_id]['quantidade']}'
            )
        
        return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))
    
    messages.success(
                request,
                f'Adicionamos {quantidade}x {produto_nome} ao seu carrinho, temos no total agora {carrinho[produto_id]['quantidade']}x'
            )
    
    request.session.save()

    return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))



    

def remover_carrinho(request):
    produto_id = request.GET.get('id', None)
    
    if not produto_id:
        return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))

    if not request.session.get('carrinho'):
        return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))
    
    if produto_id not in request.session.get('carrinho').get(str(request.user.id)):
        return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))
    
    carrinho = request.session['carrinho'][str(request.user.id)]

    messages.success(
                request,
                f'Produto {carrinho[produto_id]["nome"]} foi removido'
            )

    del carrinho[produto_id]
    request.session.save()

    return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))


@login_required(login_url='perfil:criar_perfil')
def carrinho(request):
    user_id = str(request.user.id)

    if request.session['carrinho'][str(request.user.id)]:
        carrinho = request.session['carrinho'][str(request.user.id)]
        
        context = {
        'carrinho': carrinho,
        'titulo': "Carrinho"
    }
        
        return render(request,'loja/pages/carrinho.html', context)
        
    else:
         return render(request,'loja/pages/carrinho.html')


    


    

def resumo_compra(request):
    if request.user.is_authenticated:
        perfil = Perfil.objects.filter(usuario = request.user).first()

        if request.session['carrinho'][str(request.user.id)]:
            carrinho = request.session['carrinho'][str(request.user.id)]

        if not perfil:
            messages.error(
                request,
                'Perfil não existe.'
            )
            return redirect('perfil:criar_perfil')

        if not carrinho:
            messages.error(
                request,
                'O Carrinho de compras não existe.'
            )

            return redirect('produto:index')

        context = {
            'usuario': request.user,
            'perfil': perfil,
            'carrinho': carrinho
        }

        return render(request,'loja/pages/finalizar.html', context)
    
    return redirect('perfil:criar_perfil')


def search(request):
    search = request.GET.get('search', None)

    if search == '':
        return redirect('produto:index')

    produtos = models.Produto.objects.filter(Q(nome__icontains = search) | Q(descricao_curta__icontains = search) | Q(descricao_longa__icontains = search))

    paginator = Paginator(produtos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search': search,
    }

    return render(request,'loja/pages/index.html', context)