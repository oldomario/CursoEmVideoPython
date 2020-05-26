"""
Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
numero = int(input('Em que número eu pensei? '))
while numero < 0 or numero > 5:
    print('É pra digitar entre 0 e 5!!!!')
    numero = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
sorteado = random.randint(0, 5)
if numero == sorteado:
    print('PARABÉNS!!! VOCÊ CONSEGUIU ME VENCER!!!')
else:
    print('GANHEI!!!! Eu pensei no número {} e não no {}!'.format(sorteado, numero))