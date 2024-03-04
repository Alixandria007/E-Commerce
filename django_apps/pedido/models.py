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
        return f'Pedido de {self.cliente}'
