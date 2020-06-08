'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade
de centenas, dezenas e unidades do mesmo. Observando os termos no plural a colocação
do "e", da vírgula entre outros. Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311,
111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

                            ### FUNCIONAL até 99.000 ###

n = int(input('Digite um número: '))

print('%i = '%n, end = '')

p = 0
vm, vc, vd, vu = '','','',''


## Milhar ##
m = n // 1000
if m > 0:
    p += 1
    if m == 1:
        vm = str(m) + ' milhar'
    elif m > 1:
        vm = str(m) + ' milhares'

 
## Centena ##
c = n // 100 % 10
if c > 0:
    p += 1
    if c == 1:
        vc = str(c) + ' centena'
    elif c > 1:
        vc = str(c) + ' centenas'

## Dezena ##
d = n % 100 // 10
if d > 0:
    p += 1
    if d == 1:
        vd = str(d) + ' dezena'
    elif d > 1:
        vd = str(d) + ' dezenas'

## Unidade ##
u = n % 10
if u > 0:
    p += 1
    if u == 1:
        vu = str(u) + ' unidade'
    elif u > 1:
        vu = str(u) + ' unidades'





                            ### FORMATO DE IMPRESSÃO ###

if p == 1:
    if m > 0:
        print('%s.'%(vm))
    elif c > 0:
        print('%s.'%(vc))
    elif d > 0:
        print('%s.'%(vd))
    elif u > 0:
        print('%s.'%(vu))
    
if p == 2:
    if m > 0 and c > 0:
        print('%s e %s.'%(vm,vc))
    elif c > 0 and d > 0:
        print('%s e %s.'%(vc,vd))
    elif d > 0 and u > 0:
        print('%s e %s.'%(vd,vu))
    
if p == 3:
    if m > 0 and c > 0 and d > 0:
        print('%s, %s e %s.'%(vm, vc, vd))
    if c > 0 and d > 0 and u > 0:
        print('%s, %s e %s.'%(vc, vd, vu,))      

if p == 4:
    if m > 0 and c > 0 and d > 0 and u > 0:
        print('%s, %s, %s e %s.'%(vm, vc, vd, vu))
 
    



