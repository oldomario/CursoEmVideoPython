"""
Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente.
"""
nome = str(input('Digite o nome completo: ')).strip()
nomeCompleto = nome.split()
print('First name: {}'.format(nomeCompleto[0]))
print('Last name: {}'.format(nomeCompleto[len(nomeCompleto) - 1]))