from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('pagar/<int:id>',views.pagar, name='pagar'),
    path('salvar_pedido/',views.salvar_pedido, name='salvar_pedido'),
    path('lista/',views.lista, name='lista'),
    path('detalhe/<int:pk>',views.detalhe_pedido, name='detalhe_pedido'),
]