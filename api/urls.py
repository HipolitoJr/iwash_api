from django.urls import path, include

from api.views import UsuarioView, ConsumidorView

urlpatterns = [
    path('usuarios/', UsuarioView.as_view({'get': 'list'}), name='usuarios'),
    path('consumidores/', ConsumidorView.as_view({'get': 'list'}), name='consumidores'),
]
