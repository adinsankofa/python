'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários
jogadores, incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
'''


#VERSÃO GUANABARA
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
    



#VERSÃO BRUNO
campeonato = list()
while True:
    jogo = dict()
    partidas = list()
    jogo['jogador'] = str(input('Nome do Jogador: '))
    totpart = int(input(f'Quantas partidas {jogo["jogador"]} jogou? '))
    for p in range(totpart):
        partidas.append(int(input(f"Quantos gols na partida {p+1}? " )))
    jogo['gols'] = partidas
    campeonato.append(jogo)
    while True:
        continua = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if continua in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continua == 'N':
        print('=-' * 37)
        break
    print('-' * 37)
print(f'{"cod"} {"nome":<10} {"gols":<15} {"total":<5}')
print('-' * 37)
for k, v in enumerate(campeonato):
    a = str(k)
    b = str(v['jogador'])
    c = str(v['gols'])
    d = sum(v['gols'])
    print(f'{a:>3} {b:<10} {c:<15} {d:<10}')
while True:
    print('-' * 37)
    mostra = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if mostra != 999:
        if mostra < len(campeonato):
            print(f' -- LEVANTAMENTO DO JOGADOR {campeonato[mostra]["jogador"]}: ')
            for k, v in enumerate(campeonato[mostra]['gols']):
                print(f'No jogo {k+1}', end=' ')
                print(f'fez {v} gols.')
        else:
            print(f'ERRO: Não existe o jogador com código {mostra}!')
    else:
        break
print('<< VOLTE SEMPRE >>')
  
        
    


        

    
        
        
        
        
        
        
    
        
        

