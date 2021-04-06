from rest_framework import viewsets
from ..models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewset(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer