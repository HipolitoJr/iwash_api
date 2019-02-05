from django.urls import path, include

from autenticacao.views import LoginView, LogoutView
from washes import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='login.html'), name="logout"),
]
