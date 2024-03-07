from django.core.exceptions import ValidationError


def validar_cpf(cpf: str):
    cpf = cpf.replace(".", '')
    cpf = cpf.replace('-', '')

    digit_inicial=[]
    for c in cpf:
        c=int(c)
        digit_inicial.append(c)
    soma = 0
    contador=10
    for c in digit_inicial:
        soma += c * contador
        contador-=1
        if contador<2:
            break
    digito1 = 11- (soma % 11)
    if digito1 > 9:
        digito1 = 0
    digit_inicial.append(digito1)
    soma = 0
    contador=11
    for c in digit_inicial:
        soma += c * contador
        contador-=1
        if contador<2:
            break
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    if not digit_inicial[9]==digito1 and digito2==digit_inicial[10]:
        raise ValidationError('Este cpf é invalido')
    
    return True
        



validar_cpf('57059513884')