from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.timezone import now


class Consumidor(models.Model):

    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Feminio'),
        ('O', 'Outro'),
    )

    nome_completo = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1, choices=SEXOS, blank=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')

    def name_usuario(self):
        return self.usuario.username


class Lavanderia(models.Model):

    cnpj = models.CharField(max_length=30)
    nome_fantasia = models.CharField(max_length=255, blank=False)
    endereco = models.CharField(max_length=255)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lavanderia')


class Pedido(models.Model):

    STATUS_PEDIDO = (
        ('A', 'Aguardando'),
        ('C', 'Confirmada'),
    )

    consumidor = models.ForeignKey(Consumidor, on_delete=models.CASCADE, related_name='pedidos')
    lavanderia = models.ForeignKey(Lavanderia, on_delete=models.CASCADE, related_name='pedidos')
    servico_pedido = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS_PEDIDO)
    qtd_roupas = models.IntegerField()
    observacoes = models.CharField(max_length=255)


class Solicitacao(models.Model):

    STATUS_SOLICITACAO = (
        ('A', 'Aguardando'),
        ('C', 'Confirmada'),
        ('R', 'Recusada'),
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    consumidor = models.ForeignKey(Consumidor, on_delete=models.CASCADE, related_name='solicitacoes')
    lavanderia = models.ForeignKey(Lavanderia, on_delete=models.CASCADE, related_name='solicitacoes')
    data_solicitada = models.DateField()
    servico_solicitado = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS_SOLICITACAO, default='A')

    def aceitar(self):
        self.status = 'C'
        self.save()

    def recusar(self):
        self.status = 'R'
        self.save()
