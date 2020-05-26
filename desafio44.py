"""
Elabora um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros
"""

print('*' * 5, 'PAGAMENTO DE PRODUTOS', '*' * 5)
valorProduto = float(input('Qual o valor do produto? R$'))

print('Selecione o Tipo de Pagamento:')
print('1 - À VISTA')
print('2 - PARCELADO')
tipoPagamento = int(input())

if tipoPagamento == 1:
    print('Selecione a forma de pagamento:')
    print('1 - DINHEIRO')
    print('2 - CHEQUE')
    print('3 - CARTÃO')
    formaPagamento = int(input())
    if formaPagamento == 1:
        valorFinal = valorProduto - (valorProduto*(10/100))
        print('Você ganhou um desconto de 10%. \nO valor do produto é de R${:.2f} com desconto foi para R${:.2f}'.format(valorProduto, valorFinal))
    elif formaPagamento == 2:
        valorFinal = valorProduto - (valorProduto*(10/100))
        print('Você ganhou um desconto de 10%. \nO valor do produto é de R${:.2f} com desconto foi para R${:.2f}'.format(valorProduto, valorFinal))
    elif formaPagamento == 3:
        valorFinal = valorProduto - (valorProduto*(5/100))
        print('Você ganhou um desconto de 5%. \nO valor do produto é de R${:.2f} com desconto foi para R${:.2f}'.format(valorProduto, valorFinal))

elif tipoPagamento == 2:
    print('Selecione a quantidade de parcelamento:')
    print('1 - 2x')
    print('2 - 3x ou mais')
    quantidadeParcelamento = int(input())
    if quantidadeParcelamento == 1:
        print('O valor do produto é de R${:.2f}'.format(valorProduto))
    elif quantidadeParcelamento == 2:
        vezes = int(input('Digite a quantidade de vezes: 3 ou mais: '))
        valorFinal = valorProduto + (valorProduto * (20 / 100))
        mensalidade = valorFinal/vezes
        print('\nFoi acrescentado um juros de 20% sobre o valor do produto.\n \nO valor do produto é de R${:.2f} com o acréscimo foi para R${:.2f}. \n'
              '\nVocê pagará R${:.2f} por mês durante {} meses'.format(valorProduto, valorFinal, mensalidade, vezes))