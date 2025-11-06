from .base_manager import BaseManager
from django.db import models
from typing import List


class AtletaManager(BaseManager):

    def find_by_nome(self, name: str) -> models.QuerySet['Atleta']:
        
        if not isinstance(name, str):
            raise TypeError("O nome deve ser uma string")
        return self.filter(nome__icontains=name)
    
    def buscar_participantes(self, evento_id: int) -> List['Atleta']:
        
        from analise.models import Estatistica,Atleta  

        estatisticas = Estatistica.objects.filter(evento_id=evento_id)
        atletas = [e.atleta for e in estatisticas]
        return atletas