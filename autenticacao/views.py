from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

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


