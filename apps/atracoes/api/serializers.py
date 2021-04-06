from ..models import Atracao
from rest_framework import serializers


class AtracoesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atracao
        fields = ['nome','descricao','horarios','idade_minima','aprovado','imagem']