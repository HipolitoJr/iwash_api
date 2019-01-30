from django.contrib.auth.models import User
from rest_framework import serializers
from washes.models import Consumidor, Lavanderia, Pedido, Solicitacao


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',)


class ConsumidorSerializer(serializers.ModelSerializer):

    usuario = UsuarioSerializer(read_only=False)

    class Meta:
        model = Consumidor
        fields = ('id', 'nome_completo', 'sexo', 'usuario',)