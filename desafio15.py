#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.

quantidadeDia = int(input('Digite a quantidade de dias alugado: '))
quantidadeKM = float(input('Digite a quantidade de KM percorrido: '))
valorFinal = (quantidadeDia * 60) + (quantidadeKM * 0.15)
print('O valor a pagar é de R${:.2f}'.format(valorFinal))