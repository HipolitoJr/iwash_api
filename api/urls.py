from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api.views import UsuarioView, ConsumidorView, LavanderiaView, SolicitacaoView, PedidoView

router = DefaultRouter()

router.register(r'usuarios', UsuarioView)
router.register(r'consumidores', ConsumidorView)
router.register(r'lavanderias', LavanderiaView)
router.register(r'solicitacoes', SolicitacaoView)
router.register(r'pedidos', PedidoView)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token),
]
