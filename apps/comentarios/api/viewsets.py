from rest_framework import viewsets
from ..models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewset(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer