from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import AtracoesSerializer
from ..models import Atracao
from rest_framework.filters import SearchFilter


class AtracoesViewset(viewsets.ModelViewSet):
    queryset = Atracao.objects.all().order_by('nome')
    serializer_class = AtracoesSerializer
    #Usando django-filters
    # filterset_fields = ['nome', 'descricao']
    filter_backends = (SearchFilter,)
    search_fields = ['^nome','^descricao']
    # Para realizar uma busca tendo como padrão um campo do seu banco que nao seja a ID podemos usar o atributo
    # lookup_field, mas é importante ter em mente que o campo passado deve ser uma chave unica do contrário
    # o django retornará um erro.
    # lookup_field  ='nome'
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]