from django.template import Library

register = Library()


@register.filter()
def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.',',')

@register.filter()
def quant_carrinho(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])

@register.filter()
def cart_total(carrinho):
    return sum(
        [
            item.get('preco_promo')
            if item.get('preco_promo')
            else item.get('preco')
            for item
            in carrinho.values()
        ]
    )                                                                                                             