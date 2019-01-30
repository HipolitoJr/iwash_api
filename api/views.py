from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import UsuarioSerializer, ConsumidorSerializer
from washes.models import Consumidor


class UsuarioView(viewsets.ViewSet):

    serializer_class = UsuarioSerializer

    def list(self, request):
        queryset = User.objects.all()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(PageNumberPagination(serializer.data))

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_authenticators(self):
        authentication_classes = [SessionAuthentication]
        return [auth() for auth in authentication_classes]


class ConsumidorView(viewsets.ViewSet):

    serializer_class = ConsumidorSerializer

    def list(self, request):
        queryset = Consumidor.objects.all()
        serializer = ConsumidorSerializer(queryset, many=True)
        return Response(PageNumberPagination(serializer.data))

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_authenticators(self):
        authentication_classes = [SessionAuthentication]
        return [auth() for auth in authentication_classes]
