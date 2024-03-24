from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('pagar/<int:id>',views.pagar, name='pagar'),
    path('salvar_pedido/',views.salvar_pedido, name='salvar_pedido'),
    path('lista/',views.lista_pedidos, name='lista_pedidos'),
    path('detalhe/<int:id>',views.detalhe_pedido, name='detalhe_pedido'),
]