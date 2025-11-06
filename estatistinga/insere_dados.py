from analise.models import Atleta,Evento,Estatistica
from datetime import date
from decimal import Decimal


Atleta.objects.all().delete()
Evento.objects.all().delete()
Estatistica.objects.all().delete()

atletas = [
    Atleta(
        nome="JOÃO SILVA",
        cpf="12345678901",
        email="joao.silva@example.com",
        nascimento=date(2004, 5, 12),
        nacionalidade="BRASIL",
        altura=180,
        peso=Decimal("75.5"),
        esporte="CORRIDA",
        ativo=True
    ),
    Atleta(
        nome="OLIVIO DUTRA",
        cpf="12345678902",
        email="joao.silva@example.com",
        nascimento=date(2004, 5, 12),
        nacionalidade="BRASIL",
        altura=180,
        peso=Decimal("75.5"),
        esporte="CORRIDA",
        ativo=True
    ),
    Atleta(
        nome="MARCELO SILVA",
        cpf="12345678903",
        email="joao.silva@example.com",
        nascimento=date(2004, 5, 12),
        nacionalidade="BRASIL",
        altura=180,
        peso=Decimal("75.5"),
        esporte="CORRIDA",
        ativo=True
    ),
    Atleta(
        nome="MARIA SOUZA",
        cpf="23456789012",
        email="maria.souza@example.com",
        nascimento=date(2002, 11, 3),
        nacionalidade="BRASIL",
        altura=165,
        peso=Decimal("60.3"),
        esporte="BASQUETE",
        ativo=True
    ),
    Atleta(
        nome="CARLOS LIMA",
        cpf="34567890123",
        email="carlos.lima@example.com",
        nascimento=date(2000, 4, 27),
        nacionalidade="ARGENTINA",
        altura=175,
        peso=Decimal("72.8"),
        esporte="FUTEBOL",
        ativo=True
    ),
]

for at in atletas:
    at.full_clean()  
    at.save()
    print(f" atleta criado: {at.nome} ({at.esporte})")

eventos = [Evento(
        nome="CORRIDA DE RUA 2025",
        local="Parque do Ibirapuera",
        cidade="São Paulo",
        pais="Brasil",
        data=date(2025, 12, 21),
        esporte="CORRIDA",
        oficial=True,
        organizador="Federação Paulista de Atletismo",
        capacidade=30
    ),
    
    Evento(
        nome="CAMPEONATO MUNICIPAL DE BASQUETE oficial",
        local="Ginásio do Centro Esportivo",
        cidade="Campinas",
        pais="Brasil",
        data=date(2025, 12, 15),
        esporte="BASQUETE",
        oficial=True,
        organizador="Liga de Basquete de Campinas",
        capacidade=30
    ),

    Evento(
        nome="TORNEIO DE FUTEBOL UNIVERSITÁRIO",
        local="Estádio da Universidade",
        cidade="Rio de Janeiro",
        pais="Brasil",
        data=date(2025, 12, 3),
        esporte="FUTEBOL",
        oficial=False,
        organizador="Universidade Federal do Rio de Janeiro",
        capacidade=30
)
]
for ev in eventos:
    ev.full_clean()
    ev.save()
    print(f" Evento criado: {ev.nome}")


estatistica = [ 
    Estatistica(
        atleta=Atleta.objects.get(nome="JOÃO SILVA"),
        evento=Evento.objects.get(nome="CORRIDA DE RUA 2025"),
        pontuacao=95,
        distancia=Decimal("10.50"),
        assistencias=None,
        faltas=None,
        cartoes=None,
        minutos_jogados=None
    ) ,
    Estatistica(
        atleta=Atleta.objects.get(nome="CARLOS LIMA"),
        evento=Evento.objects.get(nome="TORNEIO DE FUTEBOL UNIVERSITÁRIO"),
        pontuacao=2,
        distancia=Decimal("10.50"),
        assistencias=0,
        faltas=5,
        cartoes=2,
        minutos_jogados=35
    ),Estatistica(
        atleta=Atleta.objects.get(nome="MARIA SOUZA"),
        evento=Evento.objects.get(nome="CAMPEONATO MUNICIPAL DE BASQUETE oficial"),
        pontuacao=34,
        distancia=Decimal("10.50"),
        assistencias=10,
        faltas=2,
        cartoes=0,
        minutos_jogados=23
    ),Estatistica(
        atleta=Atleta.objects.get(nome="OLIVIO DUTRA"),
        evento=Evento.objects.get(nome="CORRIDA DE RUA 2025"),
        pontuacao=1,
        distancia=Decimal("10.50"),
        assistencias=None,
        faltas=None,
        cartoes=None,
        minutos_jogados=None
    ),
    Estatistica(
        atleta=Atleta.objects.get(nome="MARCELO SILVA"),
        evento=Evento.objects.get(nome="CORRIDA DE RUA 2025"),
        pontuacao=2,
        distancia=Decimal("10.50"),
        assistencias=None,
        faltas=None,
        cartoes=None,
        minutos_jogados=None
    )
]

for est in estatistica:
    est.full_clean()
    est.save()
    print(f"Estatistica criada com sucesso.")

parti = Atleta.objects.buscar_participantes(5)
buscaMaiores = Estatistica.objects.buscar_maiores_pontuadores_eventos_oficiais()
estran = Evento.objects.buscar_evento_participantes_estrangeiros_por_evento(date(2025, 12, 3))
vencedores = Evento.objects.corrida_winners_on(date(2025, 12, 21))


print(parti)
print(buscaMaiores)
print(estran)
print(vencedores)