"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo.
"""
r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if (r1 + r2) >= r3 and (r1 + r3) >= r2 and (r2 + r3) >= r1:
    print('Forma triângulo')
else:
    print('Não Forma triângulo')