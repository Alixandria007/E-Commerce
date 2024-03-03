from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'preco_marketing', 'preco_marketing_promocional' , 'tipo'
    prepopulated_fields = {
        'slug' : ('nome',)
    }
    