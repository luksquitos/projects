from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.serializers import Serializer
from .models import Loja, Promocao
from . import serializers

#TODO Quando o usuário mandar um post da API, não terá a limitação estabelecida no banco de dados
class TodasLojas(ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = serializers.LojaSerializer
    
@api_view()
def home(request):
    msg = 'Seja muito bem vindo a tela inicial, mesmo não tendo nada, ainda é especial'
    return Response(msg)

@api_view()
def promocoes(request):
    obj = Promocao.objects.all()
    lista = [
        serializers.PromocaoSerializer(x).data
        for x in obj
    ]
    return Response(lista)
    
        