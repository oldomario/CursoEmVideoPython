#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa
import math
catetoOposto =  float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa é: {:.2f}'.format(math.hypot(catetoOposto,catetoAdjacente)))