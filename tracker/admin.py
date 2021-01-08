from django.contrib import admin
from tracker.models import Empresa, Cliente, ProdutosVendidos, Envio,\
    Modelos, Produtos, Garantia, Eventos, Sensores, StatusDisponiveis, StatusAtual


admin.site.register(Empresa)
admin.site.register(Cliente)
admin.site.register(ProdutosVendidos)
admin.site.register(Modelos)
admin.site.register(Produtos)
admin.site.register(Garantia)
admin.site.register(Eventos)
admin.site.register(Sensores)
admin.site.register(StatusDisponiveis)
admin.site.register(StatusAtual)
admin.site.register(Envio)