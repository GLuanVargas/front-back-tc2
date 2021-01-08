from django.db import models
from django.db.models import PROTECT


class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=22)


class Cliente(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=PROTECT)
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=400)
    telefone = models.CharField(max_length=15)
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)


class Modelos(models.Model):
    nome = models.CharField(max_length=50)


class Produtos(models.Model):
    nome = models.CharField(max_length=15)
    modelo = models.ForeignKey(Modelos, on_delete=PROTECT)


class ProdutosVendidos(models.Model):
    nome = models.CharField(max_length=100)
    produto = models.ForeignKey(Produtos, on_delete=PROTECT)
    validado = models.BooleanField()
    empresa = models.ForeignKey(Empresa, on_delete=PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=PROTECT)
    chave = models.CharField(max_length=512)
    conectado = models.DateTimeField(auto_now=True)


class Garantia(models.Model):
    data_cadastro = models.DateField(auto_now_add=True)
    validade = models.DateField(auto_now_add=True)
    produto_vendido = models.ForeignKey(ProdutosVendidos, on_delete=PROTECT)


SENSORES = (
    ("cimadireita", "Cima Direita"),
    ("cimaesquerda", "Cima Esquerda"),
    ("baixoesquerda", "Baixo Esquerda"),
    ("baixodireita", "Baixo Direita"),
)


class Sensores(models.Model):
    posicao = models.CharField(max_length=30, choices=SENSORES)
    produto_vendido = models.ForeignKey(ProdutosVendidos, on_delete=PROTECT)
    status = models.IntegerField()


class Envio(models.Model):
    data = models.DateTimeField(auto_now_add=True)


class Eventos(models.Model):
    tipo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    produto_vendido = models.ForeignKey(ProdutosVendidos, on_delete=PROTECT)
    sensor = models.ForeignKey(Sensores, on_delete=PROTECT)
    envio = models.ForeignKey(Envio, on_delete=PROTECT, related_name='evento')


class StatusDisponiveis(models.Model):
    descricao = models.CharField(max_length=100)


class StatusAtual(models.Model):
    status = models.ForeignKey(StatusDisponiveis, on_delete=PROTECT)
    data = models.DateField()
    sensor = models.ForeignKey(Sensores, on_delete=PROTECT)
