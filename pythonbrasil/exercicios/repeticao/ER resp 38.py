'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior. Faça um programa que determine o salário
atual desse funcionário. Após concluir isto, altere o programa permitindo que
o usuário digite o salário inicial do funcionário.
'''


def lte(x,y,z):
    
    limite = 0
    limite2 = 0
    limite3 = 0
    
    espaço = []
    espaço2 = []
    espaço3 = []
    
    for i in range(len(x)):
        if len(x[i]) > limite:
            limite = len(x[i])
        if len(str(y[i])) > limite2:
            limite2 = len(str(y[i]))
        if len(str(z[i])) > limite3:
            limite3 = len(str(z[i]))

    for i in range(len(x)):
        dif = limite - len(x[i])
        espaço.append(dif * ' ')
        dif2 = limite2 - len(str(y[i]))
        espaço2.append(dif2 * ' ')
        dif3 = limite3 - len(str(z[i]))
        espaço3.append(dif3 * ' ')
        

    for i in range(len(x)):
        print(x[i], espaço[i] + 6 * ' ', espaço2[i], y[i], espaço3[i] + 4 * ' ', z[i])


sal = []
anos = []
percentual = []

ano_contratacao = int(input('Digite o ano da contratação: '))
ano_atual = int(input('Digite o ano atual: '))
salario_inicial = int(input('Digite o salário inicial: R$ '))

anos_trabalho = ano_atual - ano_contratacao
perc_aum = 1.5 / 100
salario = salario_inicial



print('')

print('ANO \t  AUMENTO(%) \t   SALÁRIO REAJUSTADO')
print("-" * 4, '\t', "-" * 11, '\t ', "-" * 20)
for i in range(anos_trabalho):
    
    salario += salario * perc_aum
    sal.append(salario)
    
    ano_contratacao += 1
    anos.append(str(ano_contratacao))
    
    '''
    print(ano_contratacao, '\t \t %0.3f'%perc_aum, '\t \t \t \t %0.2f'%salario)
    '''
    perc_aum *= 2
    percentual.append(perc_aum)
    
lte(anos,percentual,sal)

print('')
   
print('Salário corrigido: R$ %0.2f'%salario)    
    
