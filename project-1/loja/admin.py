from django.contrib import admin
from . import models

admin.site.register(models.Categoria)
admin.site.register(models.SubCategoria)
admin.site.register(models.Loja)
admin.site.register(models.Promocao)
admin.site.register(models.Usuario)
