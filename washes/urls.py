from django.urls import path, include
from washes import views


urlpatterns = [
    path('', views.index, name='index'),
    path('solicitacao/<int:solicitacao_id>/aceitar/', views.aceitar_solicitacao, name='aceitar_solicitacao'),
    path('solicitacao/<int:solicitacao_id>/recusar/', views.recusar_solicitacao, name='recusar_solicitacao'),

]