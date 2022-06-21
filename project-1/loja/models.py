from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.categoria

class SubCategoria(models.Model):
    subcategoria = models.ForeignKey(Categoria, models.CASCADE)

#TODO Arrumar as imagens que estão sendo mandadas para a pasta principal.    
class Loja(models.Model):
    #ForeignKey com o de cima ?
    cnpj = models.CharField(max_length=14)
    nome_fantasia = models.CharField(max_length=100)
    bio = models.TextField()
    logo = models.ImageField()
    site = models.URLField() #O que é verbosename ?
    whatsapp = models.CharField(max_length=12)
    telefone = models.CharField(max_length=12, blank=True, null=True)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    
    def __str__(self) -> str:
        return self.nome_fantasia

#usuario_loja é um método?

class Promocao(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    preco_promocao = models.DecimalField(max_digits=6, decimal_places=2)
    data_inicial = models.DateTimeField(auto_now_add=True)
    data_final = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.titulo

class Usuario(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self) -> str:
        return self.nome