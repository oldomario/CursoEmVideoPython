"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
"""
cidade = str(input('Digite a cidade em que você nasceu: ')).strip()
print('O nome da sua cidade começa com Santo? {}'.format(cidade[:5].upper() == 'SANTO'))
