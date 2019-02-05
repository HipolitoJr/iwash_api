from django.urls import path, include
from washes import views


urlpatterns = [
    path('', views.index, name='index'),
]