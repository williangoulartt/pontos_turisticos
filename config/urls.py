"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework.authtoken import views
from apps.pontos_turisticos.api.viewsets import PontoTuristicoViewSet
from apps.atracoes.api.viewsets import AtracoesViewset
from apps.avaliacoes.api.viewsets import AvaliacaoViewset
from apps.comentarios.api.viewsets import ComentarioViewset
from apps.localizacoes.api.viewsets import LocalizacaoViewset
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'ponto_turistico',PontoTuristicoViewSet,basename='PontoTuristico')
router.register(r'atracoes',AtracoesViewset)
router.register(r'avaliacoes',AvaliacaoViewset)
router.register(r'comentarios',ComentarioViewset)
router.register(r'localizacoes',LocalizacaoViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
