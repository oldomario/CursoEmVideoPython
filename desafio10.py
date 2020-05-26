#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere US$1,00 = R$3,27
dinheiro = float(input('Digite quanto você possui na carteira em reais: '))
dolar = dinheiro/3.27
print('Com o valor que possui na carteira, você pode comprar {:.2f} dolares'.format(dolar))