#Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento
salario = float(input('Digite o salário do funcionário: '))
novoSalario = salario + (salario * (15/100))
print('Salário Anterior: {:.2f} \nNovo Salário {:.2f}'.format(salario, novoSalario))