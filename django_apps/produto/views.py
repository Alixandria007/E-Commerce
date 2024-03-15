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
        'page_obj' : page_obj
    }


    return render(request,'loja/pages/index.html', context)

def detalhes(request, slug):
    produto = models.Produto.objects.filter(slug = slug).first()

    context = {
        'prod' : produto
    }

    print('Jambra')
    return render(request,'loja/pages/detail.html', context)


def adicionar_carrinho(request):
    
    produto = models.Produto.objects.all().first()
    messages.error(
        request,
        'Erro'
    )

    
    return redirect('produto:index')


    

def remover_carrinho(request):

    context = {
        'produto' : 1
    }

    return render(request,'loja/pages/detail.html', context)


def carrinho(request):

    context = {
        'produto' : 1
    }

    return render(request,'loja/pages/detail.html', context)