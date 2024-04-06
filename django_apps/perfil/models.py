from django.db import models
from django.contrib.auth.models import User
from ..utils import validador_cpf
from django.core.exceptions import ValidationError

# Create your models here.


class Perfil(models.Model):
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    idade = models.PositiveIntegerField(default = 1)
    cpf = models.CharField(max_length = 14, unique = True)
    endereco = models.CharField(max_length = 65)
    numero = models.CharField(max_length = 5)
    complemento = models.CharField(max_length = 30)
    bairro = models.CharField(max_length = 30)
    cep = models.CharField(max_length = 11)
    cidade = models.CharField(max_length = 65)
    estado = models.CharField( max_length = 2 ,choices=(
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
))
    

    def clean(self):
        error_messages = {}

        if len(self.cpf.replace('.','').replace('-',''))!=11:
            raise ValidationError(f'Erro: Você digitou {len(self.cpf.replace('.','').replace('-','.'))}digite apenas numeros e 11 characteres em seu cpf')
        
        if not self.cpf.replace('.','').replace('-','').isdigit():
            raise ValidationError('Erro: Digite apenas números em seu cpf')
        
        if not validador_cpf.validar_cpf(self.cpf):
            raise ValidationError('Cpf Invalido')
        
        return super().clean()
    
    def __str__(self):
        return self.usuario.username
