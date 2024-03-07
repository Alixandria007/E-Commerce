from typing import Any
from django.contrib import admin
from . import models
from django.utils.text import slugify

# Register your models here.

class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1

@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'preco_marketing', 'preco_marketing_promocional' , 'tipo'
    readonly_fields = 'slug',
    inlines = VariacaoInline ,

    def save_model(self, request, obj, form, change):
        slug = f'{slugify(obj.nome)}-{obj.pk}'

        obj.slug = slug


        return obj.save()



@admin.register(models.Variacao)
class VariacaoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'produto', 'preco' , 'estoque'
    