from django.contrib import admin
from . import models

# Register your models here.

class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1

@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'preco_marketing', 'preco_marketing_promocional' , 'tipo'
    prepopulated_fields = {
        'slug' : ('nome',)
    }
    inlines = VariacaoInline ,



@admin.register(models.Variacao)
class VariacaoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'produto', 'preco' , 'estoque'
    