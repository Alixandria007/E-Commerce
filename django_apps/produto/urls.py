from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('',views.index, name='index'),
    path('produto/<slug:slug>/',views.detalhes, name='detalhes'),
    path('adicionar_carrinho/',views.adicionar_carrinho, name='adicionar_carrinho'),
    path('remover_carrinho/',views.remover_carrinho, name='remover_carrinho'),
    path('carrinho/',views.carrinho, name='carrinho'),
    path('resumo_compra/',views.resumo_compra, name='resumo_compra'),
     path('search/',views.search, name='search'),
]
