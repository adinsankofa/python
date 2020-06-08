'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3%
para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas
conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
       Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

print("")
horaTrab = int(input("Horas trabalhadas: "))
valorHora = float(input("Valor da hora: "))
print("")

salBruto = valorHora * horaTrab

a = ""


if salBruto <= 900:
    IR = 0
    if IR == 0:
        a = "Isento"


elif 900 < salBruto <= 1500:
    IR = salBruto/100*5
    if salBruto/100*5:
        a = "5%"

elif 1500 < salBruto <= 2500:
    IR = salBruto/100*10
    if salBruto/100*10:
        a = "10%"

elif salBruto > 2500:
    IR = salBruto/100*5
    if salBruto/100*20:
        a = "Teto"


INSS = salBruto/100*10
FGTS = salBruto/100*11


print("======================== F O L H A   DE  P A G A M E N T O ============================")
print("")
print("\t Salário Bruto: (%i * %i)"%(valorHora, horaTrab), "\t R$ %0.2f"%(horaTrab * valorHora))
print("\t (-) IR (",a,")   \t\t :", "R$   %0.2f"%IR)
print("\t (-) INSS (10%) \t\t :", "R$  %0.2f"%(INSS))
print("\t FGTS (11%) \t\t\t :", "R$  %0.2f"%(FGTS))
print("\t Total de Descontos \t\t : R$  %0.2f"%(IR + INSS))
print("\t Salário Liquido  \t\t : R$ %0.2f"%(salBruto - IR - INSS))
print("\t Salário Bruto \t\t\t : R$ %0.2f"%(salBruto))
print('')
print("=======================================================================================")


