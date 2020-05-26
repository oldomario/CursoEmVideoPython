"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
"""
km = float(input('Digite a velocidade (km) do carro: '))
if km > 80:
    multa = (km-80)*7
    print('Velocidade acima do permitido!!! \nVocê foi multado no valor de R${:.2f}'.format(multa))
else:
    print('Dentro do limite de velocidade!!!')