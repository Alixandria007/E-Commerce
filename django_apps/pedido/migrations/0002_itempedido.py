# Generated by Django 5.0.2 on 2024-03-07 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=255)),
                ('produto_id', models.PositiveIntegerField()),
                ('variacao', models.CharField(max_length=255)),
                ('variacao_id', models.PositiveIntegerField()),
                ('preco', models.FloatField()),
                ('preco_promocional', models.FloatField(default=0)),
                ('quantidade', models.PositiveIntegerField()),
                ('imagem', models.CharField(max_length=1200)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
            ],
            options={
                'verbose_name': 'Item Pedido',
                'verbose_name_plural': 'Itens Pedidos',
            },
        ),
    ]