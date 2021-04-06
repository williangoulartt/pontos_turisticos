from rest_framework import viewsets
# from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .serializers import PontoTuristicoSerializer
from ..models import PontoTuristico


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    # queryset = PontoTuristico.objects.all().order_by('nome')
    serializer_class = PontoTuristicoSerializer

    # Este metodo é nativo do ModelViewset e é chamado quando a variavel 'queryset' nao está definida,
    # geralmente é usado para filtragens mais complexas.
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    #Sobrescrevendo metodo padrão que é acionado quando temos um GET.
    # def list(self, request, *args, **kwargs):
    #     return Response({'Teste':1234})

    # Sobrescrevendo metodo CREATE que é acionado por padrão quando temos um POST.
    # def create(self, request, *args, **kwargs):
    #     return Response({'Hello':request.data['nome']})

    # Sobrescrevendo o metodo DESTROY, este metodo é acionado quando queremos deletar
    # um recurso, sendo assim é necessário informá-lo por uma id.
    # def destroy(self, request, *args, **kwargs):
    #     pass

    # Funciona como o list, porém ele retorna um objeto baseado em filtros ou parametros que podemos
    # deixar pré estabelecidos.
    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # def update(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # Caso seja necessário realizar uma outra ação não contemplada nos métodos acima, podemos criar
    # uma função (que fará a ação necessária) e decorá-la com a funcao action(recurso do rest framework)
    # @action(methods=['post','get'],detail=True)
    # def denunciar(self,request,pk=None):
    #     pass
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]