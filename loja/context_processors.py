def carrinho_usuario(request):
    if not request.user.id:
        return {}
    
    if not request.session.get('carrinho'):
        return {}
    
    if str(request.user.id) not in request.session.get('carrinho'):
        return {}

    carrinho_usuario = {
        'carrinho': request.session['carrinho'][str(request.user.id)],
    }

    return {'carrinho_usuario' : carrinho_usuario }