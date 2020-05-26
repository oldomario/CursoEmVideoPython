"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input('Digite o valor atual do salário: '))
if salario > 1250:
    aumento = salario + salario * (10/100)
    print('O valor do salário com aumento de 10% é de R${:.2f}'.format(aumento))
else:
    aumento = salario + salario * (15 / 100)
    print('O valor do salário com aumento de 15% é de R${:.2f}'.format(aumento))
