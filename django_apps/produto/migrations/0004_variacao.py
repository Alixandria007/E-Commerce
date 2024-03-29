# Generated by Django 5.0.2 on 2024-03-03 23:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_produto_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55)),
                ('preco', models.FloatField(default=0)),
                ('preco_promocional', models.FloatField(default=0)),
                ('estoque', models.PositiveIntegerField(default=1)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
            options={
                'verbose_name': 'Variação',
                'verbose_name_plural': 'Variações',
            },
        ),
    ]
