from django.contrib.auth.models import User
from rest_framework import serializers
from washes.models import Consumidor, Lavanderia, Pedido, Solicitacao


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',)


class ConsumidorSerializer(serializers.ModelSerializer):

    #usuario = UsuarioSerializer(read_only=False)

    class Meta:
        model = Consumidor
        fields = ('id', 'nome_completo', 'sexo', 'usuario',)


class LavanderiaSerializer(serializers.ModelSerializer):

    #usuario = UsuarioSerializer(read_only=False)

    class Meta:
        model = Lavanderia
        fields = ('id', 'cnpj', 'nome_fantasia', 'endereco', 'usuario', )


class SolicitacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solicitacao
        fields = ('id', 'consumidor', 'lavanderia', 'servico_solicitado', 'status', )


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = ('id', 'consumidor', 'lavanderia', 'servico_pedido', 'status', 'qtd_roupas', 'observacoes', )