from django.db import models

class Perguntas(models.Model):
    textodapergunta = models.CharField(max_length=200)
    datadepublicacao = models.DateTimeField('data de publicação')

    def __str__(self):
        return self.textodapergunta

class Escolha(models.Model):
    pergunta = models.ForeignKey(Perguntas, on_delete=models.CASCADE, related_name='escolhas')
    textodaescolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.textodaescolha
