# Generated by Django 5.0.3 on 2024-03-23 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_pedido_qtd_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itempedido',
            name='variacao',
        ),
        migrations.RemoveField(
            model_name='itempedido',
            name='variacao_id',
        ),
    ]
