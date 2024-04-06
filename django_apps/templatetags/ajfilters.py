from django.template import Library

register = Library()


@register.filter()
def formata_preco(val):
    num = f'{val:.2f}'.replace('.', ',')
    num_format = str()
    cont = 0
    cont_int = 0

    if val >= 1000:
        for n in reversed(num):
            cont += 1
            num_format += n

            if cont >= 3 and cont_int % 3 == 0 and cont_int > 0 and cont < len(num):
                num_format += '.'
                
            if cont >= 3:
                cont_int += 1

            
        return f'R$ {num_format[::-1]}'
    
    return f'R$ {val:.2f}'.replace('.', ',')

    

@register.filter()
def formata_cpf(val):
    cpf = str()
    c = 0
    for i in val:
        

        if c % 3 == 0 and c != 0 and c != 9:
            cpf += '.'

        if c == 9:
            cpf += '-'
        cpf += i
        c += 1

    return cpf


@register.filter()
def quant_carrinho(carrinho):
    return sum([item['quantidade'] for item in dict(carrinho).values()])

@register.filter()
def cart_total(carrinho):
    return sum(
        [
            item.get('total_promo')
            if item.get('preco_promo')
            else item.get('total')
            for item
            in carrinho.values()
        ]
    ) 

@register.filter()
def trans_iter(num):
    return [x for x in range(num+1)]                                                                                                            