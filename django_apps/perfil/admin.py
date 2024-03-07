from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = 'usuario' , 'idade' , 'endereco' , 'bairro' , 'estado'