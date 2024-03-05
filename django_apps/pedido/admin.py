from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = 'cliente' , 'total' ,'status'

@admin.register(models.ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = 'produto', 'pedido' , 'preco' , 'quantidade'