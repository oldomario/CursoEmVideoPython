"""
Faça um programa que leia o nome completo de uma pessoa e diga se ela tem Silva no nome
"""
nome = str(input('Digite seu nome completo: ')).strip()
print('O seu nome possui Silva? {}'.format('SILVA' in nome.upper()))