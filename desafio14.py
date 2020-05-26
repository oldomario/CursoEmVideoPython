#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
temperatura = float(input('Digite a temperatura em Celsius: '))
fahrenheit = ((9 * temperatura) / 5) + 32
print('A temperatura de {} ºC corresponde a {} °F (Fahrenheit)'.format(temperatura, fahrenheit))