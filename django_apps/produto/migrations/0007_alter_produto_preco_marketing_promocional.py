# Generated by Django 5.0.2 on 2024-03-09 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_alter_produto_descricao_curta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(blank=True, null=True),
        ),
    ]