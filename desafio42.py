"""
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes
"""

r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if (r1 + r2) >= r3 and (r1 + r3) >= r2 and (r2 + r3) >= r1:
    print('Forma triângulo')
    if r1 == r2 == r3:
        print('Esse triângulo é Equilátero: Todos os lados iguais \nR1 {}, R2 {}, R3 {}'.format(r1, r2, r3))
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse triângulo é Isósceles: Dois lados iguais \nR1: {}, R2: {}, R3: {}'.format(r1, r2, r3))
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Esse triângulo é Escaleno: Todos os lados diferentes \nR1: {}, R2: {}, R3: {}'.format(r1, r2, r3))
else:
    print('Não Forma triângulo')