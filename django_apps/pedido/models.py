from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pedido(models.Model):
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    cliente = models.ForeignKey(User, on_delete = models.CASCADE)
    total = models.FloatField(default = 0)
    status = models.CharField(max_length = 1 ,choices = (('A' ,'Aprovado'),
                                          ('R' , 'Reprovado'),
                                          ('C', 'Criado'),
                                          ('P', 'Pendente'),
                                          ('E' , 'Enviado'),
                                          ('F' , 'Finalizado')
                                          ))
    
    def __str__(self):
        return f'Pedido Nº{self.pk}'
    
class ItemPedido(models.Model):
    class Meta:
        verbose_name_plural = 'Itens Pedidos'
        verbose_name = 'Item Pedido'

    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)
    produto = models.CharField(max_length = 255)
    produto_id = models.PositiveIntegerField()
    variacao = models.CharField(max_length = 255)
    variacao_id = models.PositiveIntegerField()
    preco = models.FloatField()
    preco_promocional = models.FloatField( default = 0)
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField( max_length = 1200)

    def __str__(self) -> str:
        return f'Item do pedido nº {self.produto}'
