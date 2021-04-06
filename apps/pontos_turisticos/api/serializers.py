from ..models import PontoTuristico
from rest_framework import serializers
from apps.atracoes.api.serializers import AtracoesSerializer


class PontoTuristicoSerializer(serializers.HyperlinkedModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    class Meta:
        model = PontoTuristico
        fields = ['nome','descricao','aprovado','imagem','atracoes']