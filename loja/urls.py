"""
URL configuration for meusite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loja, name='loja'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('adicionar-carrinho/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('aumentar-quantidade/', views.aumentar_quantidade, name='aumentar_quantidade'),
    path('diminuir-quantidade/', views.diminuir_quantidade, name='diminuir_quantidade'),
    path('remover-item/', views.remover_item, name='remover_item'),
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra')
]   
