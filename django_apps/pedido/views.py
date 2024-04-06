from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django_apps.produto.models import Produto
from django_apps.templatetags import ajfilters
from . import models

# Create your views here.

@login_required(login_url='perfil:criar_perfil')
def pagar(request, id):
    pedido = models.Pedido.objects.filter(id = id, cliente = request.user).first()

    if not pedido:
        redirect('produto:index')

    context = {
        'pedido': pedido
    }

    
    return render(request,'loja/pages/pagar.html', context)

def salvar_pedido(request):
    if not request.user.is_authenticated:
        messages.error(
            request,
            'Login requerido!'
        )
        return redirect('perfil:criar_perfil')
    
    if not request.session.get('carrinho'):
        messages.error(
            request,
            'Carrinho Vazio!'
        )
        return redirect('produto:index')
    
    carrinho_produto_id = [id for id in request.session['carrinho']]

    bd_produtos = list(Produto.objects.filter(id__in = carrinho_produto_id))

    for produto in bd_produtos:

        pid = str(produto.pk)
        estoque = produto.estoque
        quantidade = request.session['carrinho'][str(request.user.id)][pid]['quantidade']
        preco_unt = request.session['carrinho'][str(request.user.id)][pid]['preco']
        preco_promo_unt = request.session['carrinho'][str(request.user.id)][pid]['preco_promo']
        
        if estoque < quantidade:
            request.session['carrinho'][str(request.user.id)][pid]['quantidade'] = estoque
            request.session['carrinho'][str(request.user.id)][pid]['total'] = estoque * preco_unt
            request.session['carrinho'][str(request.user.id)][pid]['total_promo'] = estoque * preco_promo_unt

            messages.error(
                    request,
                    'O estoque era insuficiente, então arrumamos para você.'
                )
            
            request.session.save()
            return redirect('produto:carrinho')
        
    qtd_total_carrinho = ajfilters.quant_carrinho(request.session['carrinho'][str(request.user.id)])
    valor_total_carrinho = ajfilters.cart_total(request.session['carrinho'][str(request.user.id)])


    pedido = models.Pedido(
        cliente = request.user,
        total = valor_total_carrinho,
        qtd_total = qtd_total_carrinho,
        status = 'C'
    )

    pedido.save()

    models.ItemPedido.objects.bulk_create(
        [
            models.ItemPedido(
                pedido = pedido,
                produto = p['nome'],
                produto_id = p['id'],
                preco = p['total'],
                preco_promocional = p['total_promo'],
                quantidade = p['quantidade'],
                imagem = p['imagem'],
            )
            for p in request.session['carrinho'][str(request.user.id)].values()
        ]
    )

    del request.session['carrinho'][str(request.user.id)]
    request.session.save()

    return redirect(reverse('pedido:pagar', kwargs={'id': pedido.pk}))


@login_required(login_url='perfil:criar_perfil')
def lista_pedidos(request):
    pedidos = models.Pedido.objects.filter(cliente = request.user)

    paginator = Paginator(pedidos,10)
    page_number = request.GET.get('page',None)
    page_obj = paginator.get_page(page_number)

    context = {
        'pedidos': page_obj
    }
    return render(request,'loja/pages/lista_pedidos.html', context)

@login_required(login_url='perfil:criar_perfil')
def detalhe_pedido(request, id):
    pedido = models.Pedido.objects.filter(id = id , cliente = request.user).first()

    context = {
        'pedido': pedido
    }

    return render(request,'loja/pages/detalhe_pedido.html', context)