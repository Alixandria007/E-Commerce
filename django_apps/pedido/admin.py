from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = 'cliente' , 'total' ,'status'