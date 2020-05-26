"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
"""
import time
while True:
    numero = int(input('Escreva um número inteiro qualquer: '))

    print('\nSelecione a opção para conversão do seu número:')
    print('1 - BINÁRIO')
    print('2 - OCTAL')
    print('3 - HEXADECIMAL')
    opcao = int(input())
    print('\nCONVERTENDO O NÚMERO...')
    time.sleep(2)
    if opcao == 1:
        binario = bin(numero)[2:]
        print('\nO número {} em binário é {}'.format(numero, binario))
        break
    elif opcao == 2:
        octal = oct(numero)[2:]
        print('\nO número {} em octal é {}'.format(numero, octal))
        break
    elif opcao == 3:
        hexadecimal = hex(numero)[2:]
        print('\nO número {} em hexadecimal é {}'.format(numero, hexadecimal))
        break
    else:
        print('Opção Inválida!!!')
