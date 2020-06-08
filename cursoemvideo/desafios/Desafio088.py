# VERSÃO GUANABARA
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('       JOGA NA MEGA SENA       ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)



# VERSÃO BRUNO
from random import randint
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
quant_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('{:^30}'.format(f'SORTEANDO {quant_jogos} JOGOS'))
megasena = []
for i in range(1, quant_jogos+1):
    sorteados = []
    for c in range(1, quant_jogos+1):
        numero = randint(1,60)
        while True:
            if numero not in sorteados:
                sorteados.append(numero)
                break
            else:
                numero = randint(1,60)
                sorteados.append(numero)
                break
    sorteados.sort()
    megasena.append(sorteados)
for i in range(len(megasena)):
    print(f'Jogo {i+1}: {megasena[i]}')
print('{:^30}'.format(f'< BOA SORTE !!! >'))


    
        
        
    
