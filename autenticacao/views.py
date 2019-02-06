from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from washes.models import Lavanderia
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class LoginView(TemplateView):

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        try:
            if user is not None and user.lavanderia:
                login(request, user=user)
                return redirect('index')
            else:
                return render(request, 'login.html')
        except Exception:
            return render(request, 'login.html')

        return render(request, self.template_name)


class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return render(request, self.template_name)

    def post(self, request):
        logout(request)
        return render(request, self.template_name)



class SignUpView(TemplateView):

    def get(self, request):
        return render(request, 'sign_up.html' )

    @transaction.atomic()
    def post(self,request):
        dados = request.POST
        senha = make_password("%s" % dados['password'])
        print(dados['password'])

        usuario = User(username = dados['username'],
                    first_name = '',
                    last_name = '',
                    email = dados['email'],
                    password=senha,
                    last_login = timezone.now(),
                    is_superuser = False,
                    is_staff = True,
                    is_active = True,
                    date_joined = timezone.now())
        usuario.save()
        lavanderia = Lavanderia(cnpj=dados['cnpj'],
                                nome_fantasia=dados['nome_fantasia'],
                                endereco=dados['endereco'],
                                usuario_id=usuario.id)
        lavanderia.save()

        messages.success(request, 'Lavanderia cadastrada com sucesso!')

        return redirect('/sign/login/')


