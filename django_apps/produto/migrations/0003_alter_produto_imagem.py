# Generated by Django 5.0.2 on 2024-03-03 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(upload_to='prod/imgs/%Y/%m/'),
        ),
    ]
