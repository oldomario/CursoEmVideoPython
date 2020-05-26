"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valorCasa = float(input('Qual o valor da casa? R$'))
salarioComprador = float(input('Qual o salário do comprador? R$'))
anosPagar = int(input('Quantos anos ele vai pagar? '))

quantidadeMeses = anosPagar * 12
mensalidade = valorCasa / quantidadeMeses
mensalidadeComprador = salarioComprador * 30/100

print('O valor da prestação durante {} anos é de R${:.2f} por mês'.format(anosPagar, mensalidade))

if mensalidade > mensalidadeComprador:
    print('Infelizmente você não pode financiar essa casa!')
else:
    print('Você consegue financiar a casa pois a parcela é até 30% do seu salário!!!')
