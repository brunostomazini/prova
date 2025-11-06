from .base_manager import BaseManager
from django.db import models
from datetime import date
from typing import List


class EventoManager(BaseManager):

    def corrida_winners_on(self, data: date) -> List['Atleta']:

        from analise.models import Estatistica, Evento  # local imports to avoid circular import

        eventos = Evento.objects.filter(data=data, esporte__icontains="CORRIDA")
        vencedores = []

        for evento in eventos:
            estatisticas = Estatistica.objects.filter(evento=evento).order_by('pontuacao')
            if estatisticas.exists():
                vencedores.append(estatisticas.first().atleta)

        return vencedores

    def buscar_evento_participantes_estrangeiros_por_evento(self, data: date) -> list['Atleta']:
        from analise.models import Evento, Atleta

        atletas_estrangeiros = Atleta.objects.filter(
            estatisticas__evento__data=data
        ).exclude(
            nacionalidade__iexact="BRASIL"
        ).distinct()
        return atletas_estrangeiros
    def find_by_nome(self, name: str) -> models.QuerySet['Evento']:
        
        from analise.models import Evento
        if not isinstance(name, str):
            raise TypeError("O nome deve ser uma string")
        return self.filter(nome__icontains=name)
    
    