'''
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou.
Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo
salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos,
impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário
igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a
regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
'''


                ### ALGORITMO ###

print('\n')
print('Projeção de Gastos com Abono')
print('=' * 28)

print('')

salario = []
sal = 1

while sal != 0:
    sal = float(input('Salário: '))
    if sal > 0:
        salario.append(sal)

print('')

print('Salário', ' ' * 3, ' - ', 'Abono')

abono_porc = []
espaço1 = []
espaço2 = []
limite1 = 0
limite2 = 0
Dif1 = 0
Dif2 = 0
teto = 100
nteto = 0
abono = []

for i in range(len(salario)):

    perc = salario[i] / 100 * 20
    
    if salario[i] < 1000:
        nteto += 1
        abono_porc.append('%0.2f'%teto)
        abono.append(teto)
    else:
        abono_porc.append('%0.2f'%perc)
        abono.append(perc)
        
    if len(str(salario[i])) > limite1:
        limite1 = len(str(salario[i]))
    if len(str(abono_porc[i])) > limite2:
        limite2 = len(str(abono_porc[i]))

for i in range(len(salario)):
    Dif1 = limite1 - len(str(salario[i]))
    espaço1.append(Dif1 * ' ')
    Dif2 = limite2 - len(str(abono_porc[i]))
    espaço2.append(Dif2 * ' ')

   
for i in range(len(salario)):
    print('R$',espaço1[i],'%0.2f'%salario[i], '-', 'R$',espaço2[i],abono_porc[i])

print('')

print('Foram processados %i trabalhadores '%(len(salario)))
print('Total gasto com abonos: R$ %0.2f'%(sum(abono)))
print('Valor mínimo pago a %i trabalhadores '%(nteto))
print('Maior valor de abono pago: R$ %0.2f'%(max(abono)))

print('\n')
