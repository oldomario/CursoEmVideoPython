#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura*altura
qtdTinta = area/2
print('O valor total da área é de: {} metros² e a quantidade de tinta necessária para pintá-la é de: {} litros'.format(area, qtdTinta))
