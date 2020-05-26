"""
Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM
e R$0,45 para viagens mais longas.
"""
distancia = float(input('Digite a distância da viagem em KM: '))
if distancia <= 200:
    valorPassagem = distancia * 0.5
    print('O valor da sua passagem é de R${:.2f}'.format(valorPassagem))
else:
    valorPassagem = distancia * 0.45
    print('O valor da sua passagem é de R${:.2f}'.format(valorPassagem))