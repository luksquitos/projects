from rest_framework import serializers
from .models import *

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['id', 'cnpj', 'nome_fantasia', 'bio', 'logo', 'site', 'whatsapp', 'telefone', 'cidade', 'uf']

class PromocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocao
        fields = ['id', 'loja', 'titulo', 'descricao', 'preco', 'preco_promocao', 'data_inicial', 'data_final']