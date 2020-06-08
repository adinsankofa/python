'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

#VERSÃO GUANABARA
jogador = dict()
partidas = list()
jogador['nome'] = str(input("Nome do Jogador: "))
tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for i in range(0, tot):
    partidas.append(int(input(f"Quantos gols na partida {i}? " )))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print("=-" * 30)
print(jogador)
print("=-" * 30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("=-" * 30)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for k, v in enumerate(jogador['gols']):
    print(f" => Na partida {k}, fez {v} gols.")
print(f"Foi um total de {jogador['total']} gols.")



#VERSÃO BRUNO
jogo = dict()
jogo['nome'] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {jogo['nome']} jogou? "))
listagols = list()
for i in range(partidas):
    gol = int(input(f"Quantos gols na partida {i}? " ))
    listagols.append(gol)
jogo['gols'] = listagols
jogo['total'] = sum(listagols)
print("=-" * 30)
print(jogo)
print("=-" * 30)
for k, v in jogo.items():
    print(f"O campo {k} tem o valor {v}")
print("=-" * 30)
print(f"O jogador {jogo['nome']} jogou {partidas} partidas.")
for k, v in enumerate(listagols):
    print(f" => Na partida {k}, fez {v} gols.")
print(f"Foi um total de {jogo['total']} gols.")
