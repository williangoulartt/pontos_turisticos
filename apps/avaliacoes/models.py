from django.db import models
from django.contrib.auth.models import User


class Avaliacao(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    avaliacao = models.TextField(null=True,blank=True)
    pontuacao = models.DecimalField(decimal_places=2,max_digits=3)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
