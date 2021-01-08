from django.views.generic import TemplateView
from rest_framework import viewsets
from tracker.models import Envio, ProdutosVendidos, Eventos
from tracker.serializers import EnvioSerializer, ConectadoSerializer


class EnviosViewSet(viewsets.ModelViewSet):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer


class ConectadoViewSet(viewsets.ModelViewSet):
    queryset = ProdutosVendidos.objects.all()
    serializer_class = ConectadoSerializer


class ListView(TemplateView):

    template_name = "produtos_lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ultimo_envio_dados = Envio.objects.all().values(
            'id',
            'data',
            'evento__valor',
            'evento__produto_vendido__produto__nome',
            'evento__produto_vendido__produto__id'
        )
        listagem = []
        for envio in ultimo_envio_dados:
            sensor1_valor = Eventos.objects.filter(envio=envio['id'], sensor__posicao="cimadireita").values("valor")
            sensor2_valor = Eventos.objects.filter(envio=envio['id'], sensor__posicao="cimaesquerda").values("valor")
            sensor3_valor = Eventos.objects.filter(envio=envio['id'], sensor__posicao="baixodireita").values("valor")
            sensor4_valor = Eventos.objects.filter(envio=envio['id'], sensor__posicao="baixoesquerda").values("valor")
            sensor1_valor = sensor1_valor[0]['valor'] if sensor1_valor.count() > 0 else 0
            sensor2_valor = sensor2_valor[0]['valor'] if sensor2_valor.count() > 0 else 0
            sensor3_valor = sensor3_valor[0]['valor'] if sensor3_valor.count() > 0 else 0
            sensor4_valor = sensor4_valor[0]['valor'] if sensor4_valor.count() > 0 else 0
            env = {
                "id":envio['evento__produto_vendido__produto__id'],
                "nome":envio['evento__produto_vendido__produto__nome'],
                "data": envio['data'].strftime("%d/%m/%Y  %H:%M:%S"),
                "sensor1": float(sensor1_valor),
                "sensor2": float(sensor2_valor),
                "sensor3": float(sensor3_valor),
                "sensor4": float(sensor4_valor),
                "peso_total":"Não informado",
                "avaliacao": "Não informada",
                "maior_desvio": "Não informado"
            }
            peso_total = env['sensor1'] + env['sensor2'] + env['sensor3'] + env['sensor4']
            percentual_sensor1 = (peso_total * env['sensor1']) / 100
            percentual_sensor2 = (peso_total * env['sensor2']) / 100
            percentual_sensor3 = (peso_total * env['sensor3']) / 100
            percentual_sensor4 = (peso_total * env['sensor4']) / 100
            maior_desvio = percentual_sensor1
            maior_desvio = percentual_sensor2 if percentual_sensor2 > maior_desvio else maior_desvio
            maior_desvio = percentual_sensor3 if percentual_sensor3 > maior_desvio else maior_desvio
            maior_desvio = percentual_sensor4 if percentual_sensor4 > maior_desvio else maior_desvio
            env['maior_desvio'] = round(maior_desvio, 2)
            env['peso_total'] = round(peso_total, 2)
            env['avaliacao'] = "Adequada" if maior_desvio < 30 else "Atenção" if maior_desvio < 35 else "Incorreta"
            if env['maior_desvio'] == 0:
                env['avaliacao'] = "Não avaliada"
            listagem.append(env)
        context['produtos'] = listagem
        return context