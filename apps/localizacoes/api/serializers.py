from rest_framework import serializers
from ..models import Localizacao


class LocalizacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Localizacao
        fields = ['latitude','longitude']