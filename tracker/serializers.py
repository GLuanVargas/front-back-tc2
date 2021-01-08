from drf_writable_nested import NestedCreateMixin, NestedUpdateMixin
from rest_framework import serializers
from tracker.models import Eventos, Envio, ProdutosVendidos


class EventosSerializer(NestedUpdateMixin, NestedCreateMixin, serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = (['sensor', 'produto_vendido', 'valor', 'tipo'])


class EnvioSerializer(NestedUpdateMixin, NestedCreateMixin, serializers.ModelSerializer):
    evento = EventosSerializer(many=True)

    class Meta:
        model = Envio
        fields = (['evento'])


class ConectadoSerializer(NestedUpdateMixin, NestedCreateMixin, serializers.ModelSerializer):

    class Meta:
        model = ProdutosVendidos
        fields = (['id', 'conectado'])