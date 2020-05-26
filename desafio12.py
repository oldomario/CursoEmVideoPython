#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
produto = float(input('Digite o preço de um produto: '))
novoValor = produto - ((5/100)*produto)
print('O valor do produto com 5% de desconto é: {} reais'.format(novoValor))