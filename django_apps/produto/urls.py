from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('',views.index, name='index'),
    path('<slug:slug>/',views.detalhes, name='detalhes'),
    path('adicionar_carrinho/',views.index, name='adicionar_carrinho'),
    path('remover_carrinho/',views.index, name='remover_carrinho'),
    path('carrinho/',views.index, name='carrinho'),
    path('finalizar/',views.index, name='finalizar'),
]
