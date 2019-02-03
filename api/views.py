from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import UsuarioSerializer, ConsumidorSerializer, LavanderiaSerializer, SolicitacaoSerializer, PedidoSerializer
from washes.models import Consumidor, Lavanderia, Solicitacao, Pedido


class UsuarioView(viewsets.ModelViewSet):

    serializer_class = UsuarioSerializer
    queryset = User.objects.all()


class ConsumidorView(viewsets.ModelViewSet):

    serializer_class = ConsumidorSerializer
    queryset = Consumidor.objects.all()


class LavanderiaView(viewsets.ModelViewSet):

    serializer_class = LavanderiaSerializer
    queryset = Lavanderia.objects.all()


class SolicitacaoView(viewsets.ModelViewSet):

    serializer_class = SolicitacaoSerializer
    queryset = Solicitacao.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Solicitacao.objects.all()

        try:
            if user.perfil:
                queryset = Solicitacao.objects.filter(consumidor=user.id)
            elif user.lavanderia:
                queryset = Solicitacao.objects.filter(lavanderia=user.id)
        except AttributeError:
            queryset = Solicitacao.objects.all()

        return queryset


class PedidoView(viewsets.ModelViewSet):

    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Pedido.objects.all()

        try:
            if user.perfil:
                queryset = Pedido.objects.filter(consumidor=user.id)
            elif user.lavanderia:
                queryset = Pedido.objects.filter(lavanderia=user.id)
        except AttributeError:
            queryset = Pedido.objects.all()

        return queryset