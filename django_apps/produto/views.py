from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from . import models
# Create your views here.

def index(request):
    produtos = models.Produto.objects.all().order_by('-pk')

    paginator = Paginator(produtos,10)
    page_number = request.GET.get('page',None)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
    }


    return render(request,'loja/pages/index.html', context)

def detalhes(request, slug):
    produto = models.Produto.objects.filter(slug = slug).first()

    context = {
        'prod' : produto
    }

    return render(request,'loja/pages/detail.html', context)


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
    quantidade = 1
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
    

    if not request.session.get('carrinho'):
        request.session['carrinho'] = {}
        request.session.save()

    carrinho = request.session['carrinho']

    if produto_id in carrinho:
        quantidade_carrinho = carrinho[produto_id]['quantidade']
        quantidade_carrinho += 1

        if produto_estoque < quantidade_carrinho:
            messages.warning(
                request,
                f'Estoque insuficiente para {quantidade_carrinho} no {produto_nome}, Adicionamos {produto_estoque} ao Carrinho' 
            )
            quantidade_carrinho = produto_estoque

        carrinho[produto_id]['quantidade'] = quantidade_carrinho 
        carrinho[produto_id]['preco'] = preco_unico * quantidade_carrinho
        carrinho[produto_id]['preco_promo'] = preco_unico_promo * quantidade_carrinho

    else:
        carrinho[produto_id] = {
            'id': produto_id,
            'nome': produto_nome,
            'preco': preco_unico,
            'preco_promo': preco_unico_promo,
            'quantidade' : quantidade,
            'slug' : slug,
            'imagem' : imagem
        }

        request.session.save()
        
        messages.success(
                request,
                f'Produto {produto_nome} adicionado ao seu '
                f'carrinho {carrinho[produto_id]["quantidade"]}.'
            )
        
        return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))
    
    messages.success(
                request,
                f'Produto {produto_nome} adicionado ao seu '
                f'carrinho {carrinho[produto_id]["quantidade"]}.'
            )
    
    request.session.save()
    return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))



    

def remover_carrinho(request):
    produto_id = request.GET.get('id', None)
    
    if not produto_id:
        return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))

    if not request.session.get('carrinho'):
        return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))
    
    if produto_id not in request.session.get('carrinho'):
        return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))
    
    carrinho = request.session.get('carrinho')

    messages.success(
                request,
                f'Produto {carrinho[produto_id]["nome"]} foi removido'
            )

    del carrinho[produto_id]
    request.session.save()
    return redirect(request.META.get('HTTP_REFERER', reverse('produto:index')))


def carrinho(request):
    
    context = {
        
    }
    return render(request,'loja/pages/carrinho.html', context)

def resumo_compra(request):
    ...