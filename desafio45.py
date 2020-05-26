"""
Crie um programa que faça o computador jogar Jokenpô com você
"""
from random import randint
from time import sleep

itens = ('Papel', 'Pedra', 'Tesoura')
computador = randint(0,2)

print('*' * 36)
print('*' * 5, 'VAMOS BRINCAR DE JOKENPÔ', '*' * 5)
print('*' * 36)
print('Escolha uma opção abaixo:')
print('[1] - Papel')
print('[2] - Pedra')
print('[3] - Tesoura')

jogador = int(input('Qual sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('*' * 20)
print('JOGADA JOGADOR: {}'.format(itens[jogador - 1]))
print('JOGADA COMPUTADOR: {}'.format(itens[computador]))
print('*' * 20)



if computador == 0:
    if jogador == 1:
        print('Deu empate!')
    elif jogador == 2:
        print('O computador venceu!')
    elif jogador == 3:
        print('Você venceu!')
    else:
        print('Opção inválida!')

if computador == 1:
    if jogador == 1:
        print('Você venceu!')
    elif jogador == 2:
        print('Deu empate!')
    elif jogador == 3:
        print('O computador venceu!')
    else:
        print('Opção inválida!')

if computador == 2:
    if jogador == 1:
        print('O computador venceu!')
    elif jogador == 2:
        print('Você venceu!')
    elif jogador == 3:
        print('Deu empate!')
    else:
        print('Opção inválida!')