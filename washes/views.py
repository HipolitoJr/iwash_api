from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def index(request):
    solicitacoes = request.user.lavanderia.solicitacoes.all()
    return render(request, 'index.html', {'solicitacoes': solicitacoes})