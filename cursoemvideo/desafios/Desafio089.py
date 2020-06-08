# VERSÃO GUANABARA
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')




# VERSÃO BRUNO
cont = 0
nome = []
nota = []
aluno = []
while True:
    nota.append(str(input("Nome: ")))
    for i in range(2):
        nota.append(float(input(f"Nota {i+1}: ")))
    aluno.append(nota)
    nota = []
    cont = str(input("Quer continuar? [S/N] ")).upper()
    if "N" in cont:
        break
    print()
print('=-' * 15)

print('Nº.  NOME \t MÉDIA')
print('-' * 30)
for i in range(len(aluno)):
    print(f'{i}    {aluno[i][0]} \t {(sum(aluno[i][1:]) / 2)}')
print('-' * 50)

while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas == 999:
        break
    else:
        print(f'Notas de {aluno[notas][0]} são {aluno[notas][1:]}')
        print('-' * 50)
print('-' * 50)    

                    
    
        
        
    
