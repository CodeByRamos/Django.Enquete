# Generated by Django 5.1.4 on 2025-01-18 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enquete', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perguntas',
            name='datadepublicacao',
            field=models.DateTimeField(verbose_name='data de publicação'),
        ),
        migrations.CreateModel(
            name='Escolha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textodaescolha', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escolhas', to='Enquete.perguntas')),
            ],
        ),
        migrations.DeleteModel(
            name='Alternativa',
        ),
    ]
