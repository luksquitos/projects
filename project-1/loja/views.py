from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.serializers import Serializer
from .models import Loja, Promocao, Usuario
from . import serializers

#FIXME POST na API_VIEW não tem a limitação do banco de dados
class TodasLojas(ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = serializers.LojaSerializer
    
@api_view()
def home(request):
    return Response({
        404: "Not Found",
        "url_1": "lojas/",
        "url_2": "promocoes/",
        "url_3": "usuarios/",
    })

@api_view()
def promocoes(request):
    
    #Se fornecido parâmetro via URL,
    #irá mostrar promoções da respectiva loja.
    
    loja_id = request.GET.get('loja_id', '')
    if loja_id:
        loja_id = int(loja_id)
        loja_promocao = Promocao.objects.filter(loja_id=loja_id)
        if not loja_promocao:
            return Response({404: "Not Found"})
        return Response(serializers.PromocaoSerializer(
                                        loja_promocao,
                                        many=True).data
                                )
    
    #Caso contrario mostrará todas as promoções disponíveis
    
    else:
        obj = Promocao.objects.all()
        return Response(serializers.PromocaoSerializer(obj, many=True).data)
                                         
@api_view()                                  
def usuario(request):
    
    #Se fornecido parâmetro via URL, 
    # irá mostrar todas as lojas que o usuário segue.   
    
    user_id = request.GET.get('user_id', '')
    if user_id:
        try:
            usuario = Usuario.objects.get(id=int(user_id))                
        except:
            return Response({
                404: "Not Found"
            })
        todas_lojas = []
        for loja in usuario.loja.all():
            json_data = {
                "id": loja.id,
                "cnpj": loja.cnpj,
                "nome_fantasia": loja.nome_fantasia,
                "bio": loja.bio,
                "logo": "não sei como colocar",
                "site": loja.site,
                "whatsapp": loja.whatsapp,
                "telefone": loja.telefone,
                "cidade": loja.cidade,
                "uf": loja.uf 
            }
            todas_lojas.append(json_data)
        return Response(todas_lojas)
    
    #Caso contrario, mostrará apenas as pessoas cadastradas
    
    else:
        all_users = Usuario.objects.all()
        list_users = []
        for user in all_users:
            json_data= {
                "id": user.id,
                # "loja": user.loja,    #Essa linha quebrou, como eu esperava.
                "nome": user.nome,
                "email": user.email
            }
            list_users.append(json_data)
        return Response(list_users)