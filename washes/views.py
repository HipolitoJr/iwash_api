from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from washes.models import Solicitacao


@login_required
def index(request):
    solicitacoes = request.user.lavanderia.solicitacoes.order_by('status').exclude(status='R')
    return render(request, 'index.html', {'solicitacoes': solicitacoes})

def aceitar_solicitacao(request, solicitacao_id):
    solicitacao = Solicitacao.objects.get(id=solicitacao_id)
    solicitacao.aceitar()
    return redirect('index')

def recusar_solicitacao(request, solicitacao_id):
    solicitacao = Solicitacao.objects.get(id=solicitacao_id)
    solicitacao.recusar()
    return redirect('index')