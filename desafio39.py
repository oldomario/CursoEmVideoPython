"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import datetime
ano = int(input('Digite o ano de nascimento: '))
idade = datetime.now().year - ano

if idade < 18:
    tempoFaltante = 18 - idade
    print('Você deverá alistar ao serviço militar daqui a {} ano(s)!'.format(tempoFaltante))
elif idade == 18:
    print('Já é hora de se alistar ao serviço militar!!!')
else:
    prazoExpirado = idade - 18
    print('Seu tempo de alistamento já passou! \nVocê deveria ter se alistado a {} ano(s) atrás!'.format(prazoExpirado))