from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('pagar/',views.index, name='pagar'),
    path('fechar_pedido/',views.index, name='fechar_pedido'),
    path('detalhe/<int:pk>',views.index, name='detalhe'),
]