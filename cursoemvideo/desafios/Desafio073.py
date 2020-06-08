'''
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
'''


## VERSÃO GUANABARA:

times = ('Palmeiras', 'Santos', 'Atlético', 'Botafogo', 'Flamengo',
         'Bahia', 'Internacional', 'São Paulo', 'Corinthians', 'Athletico-PR',
         'Ceará SC', 'Goiás', 'Grêmio', 'Cruzeiro', 'Chapecoense', 'Fluminense',
         'Fortaleza', 'Vasco da Gama', 'CSA', 'Avaí')


print(f"Lista de Times: {times}")

print("-=" * 40)

print("")
print(f"A) Os 5 primeiros: {times[0:4]}")

print("\n")
print("-=" * 40)

print(f"\nB) Os últimos 4 colocados: {times[-4:]}")

print("\n")
print("-=" * 40)

print(f"\nC) Times em ordem alfabética: {sorted(times)}") ## sorted não muda a tupla, apenas a exibição

print("\n")
print("-=" * 40)

print(f"\nD) Em que posição está o time da Chepecoense: {times.index('Chapecoense')+1}ª posição")
    
print("")
print("-=" * 40)






## VERSÃO BRUNO:
'''
times = ('Palmeiras', 'Santos', 'Atlético', 'Botafogo', 'Flamengo',
         'Bahia', 'Internacional', 'São Paulo', 'Corinthians', 'Athletico-PR',
         'Ceará SC', 'Goiás', 'Grêmio', 'Cruzeiro', 'Chapecoense', 'Fluminense',
         'Fortaleza', 'Vasco da Gama', 'CSA', 'Avaí')


print(f"Lista de Times: {times}")

print("-=" * 40)

print("")
print("A) Os 5 primeiros: ", end="")
i=0
while i < 5:
    print(times[i], end=", ")
    i+=1

print("\n")
print("-=" * 40)

print("\nB) Os últimos 4 colocados: ", end="")
for i in range(len(times)-4, len(times)):
    print(times[i], end=", ")

print("\n")
print("-=" * 40)

print("\nC) Times em ordem alfabética: ", end="")
timesprov = []
for i in times:
    time = i
    timesprov.append(time)
timesprov.sort()
times_ordem = ()
for i in range(len(timesprov)):
    time = timesprov[i]
    times_ordem = times_ordem + (time,)
for i in times_ordem:
    print(i, end=", ")

print("\n")
print("-=" * 40)

print("\nD) Em que posição está o time da Chepecoense: ", end="")
for i in range(len(times)):
    if times[i] == 'Chapecoense':
        print("{}º colocado".format(i+1))
    else:
        pass
    
print("")
print("-=" * 40)
'''
