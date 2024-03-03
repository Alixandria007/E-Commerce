from typing import Iterable
from django.db import models
from ..utils import imgs

# Create your models here.

class Produto(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    nome = models.CharField(max_length = 55 , blank = False)
    slug = models.SlugField(unique = True)
    descricao_longa = models.TextField(max_length = 255)
    descricao_curta = models.TextField(max_length = 60)
    imagem = models.ImageField(upload_to='prod/imgs/%Y/%m/', blank = False , null = False)
    preco_marketing = models.FloatField(default = 0)
    preco_marketing_promocional = models.FloatField(default = 0)
    tipo = models.CharField( 
        default = 'V',
        max_length = 1,
        choices = (
            ('V' , 'Variação'),
            ('S' , 'Simples')
        ),
    )

    def save(self, *args,  **kwargs):
        img_name = str(self.imagem.name)
        super_save = super().save(*args, **kwargs)
        img_changed = False

        if self.imagem:
            img_changed = img_name != self.imagem.name

        if img_changed:
            self.imagem = imgs.resize_imgs(self.imagem , 500 , True, 70)

        return super_save

