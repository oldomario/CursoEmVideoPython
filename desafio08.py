#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
metro = float(input('Digite o tamanho do metro: '))
centimetros = metro*100
milimetros = metro*1000
print('{} metros possuem {} centímetros e {} milímetros'.format(metro,centimetros,milimetros))