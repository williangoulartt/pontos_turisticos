from rest_framework import viewsets
from .serializers import LocalizacaoSerializer
from ..models import Localizacao


class LocalizacaoViewset(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer