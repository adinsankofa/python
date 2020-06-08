"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

def reaj():

    x = 280
    y = 700
    z = 1500

    salarioAtual = 0

    if salarioAntigo >= 1 and salarioAntigo < x:
        salarioAtual = salarioAntigo * 0.20
    else:
        if salarioAntigo > x and salarioAntigo <= y:
            salarioAtual = salarioAntigo * 0.15
        else:
            if salarioAntigo > y and salarioAntigo <= z:
                salarioAtual = salarioAntigo * 0.10
            else:
                if salarioAntigo > z:
                    salarioAtual = salarioAntigo * 0.05

    return salarioAtual


print("")    
salarioAntigo = float(input("Digite o salário atual: R$ " ))

a = reaj()

b = salarioAntigo + a

c = (b / salarioAntigo)-1


print("")
print(" ================================================================")
print("|\t\tDEMONSTRATIVO DE AUMENTO\t\t\t |")
print(" ================================================================")
print("|\t Seu salário anterior ao reajuste: R$ %0.2f"%salarioAntigo, "\t\t |")
print("|\t Percentual de aumento aplicado: %0.2f"%(c * 100), "%", "\t\t |")
print("|\t Valor do aumento: R$ %0.2f"%a, "\t\t\t\t |")
print("|\t Novo salário: R$ %0.2f"%(salarioAntigo + a), "\t\t\t\t |")
print(" ================================================================")



