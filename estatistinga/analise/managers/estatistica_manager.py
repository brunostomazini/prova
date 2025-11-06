from .base_manager import BaseManager
from django.db import models
from typing import List


class EstatisticaManager(BaseManager):

    def buscar_maiores_pontuadores_eventos_oficiais(self) -> List['Atleta']:

        from analise.models import Estatistica

        estatisticas = Estatistica.objects.filter(
            evento__nome__icontains='oficial'
        ).order_by('-pontuacao')

        atletas = [e.atleta for e in estatisticas]
        return atletas