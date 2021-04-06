from django.db import models


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horarios = models.TextField()
    idade_minima = models.IntegerField()
    aprovado = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='atracoes',blank=True,null=True)

    def __str__(self):
        return self.nome

