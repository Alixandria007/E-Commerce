from django.shortcuts import render
from django.core.paginator import Paginator
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
        'produto' : produto
    }

    return render(request,'loja/pages/detail.html', context)