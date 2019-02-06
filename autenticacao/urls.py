from django.urls import path, include

from autenticacao.views import LoginView, LogoutView, SignUpView
from washes import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('sign-up/',SignUpView.as_view(template_name='sign_up.html'),name="sign_up"),
    path('logout/', LogoutView.as_view(template_name='login.html'), name="logout"),
]
