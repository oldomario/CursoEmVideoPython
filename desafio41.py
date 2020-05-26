"""
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
até 9 anos: Morim
até 14 anos: Infantil
até 19 anos: Junior
até 20 anos: Sênior
acima: Master
"""
from datetime import datetime

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = datetime.now().year - ano
if idade <= 9:
    print('Categoria Mirim')
elif idade > 9 and idade <= 14:
    print('Categoria Infantil')
elif idade > 14 and idade <= 19:
    print('Categoria Junior')
elif idade == 20:
    print('Categoria Sênior')
elif idade >20:
    print('Categoria Master')