'''
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

# VERSÃO GUANABARA:
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")
    


# VERSÃO BRUNO:
eq = list()
expressao = str(input("Digite uma expressão: "))
eq.append(expressao)
parenteses = 0
for i in eq[0]:
    if i == "(" or i == ")":
        parenteses += 1
    else:
        pass
if parenteses % 2 == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")


