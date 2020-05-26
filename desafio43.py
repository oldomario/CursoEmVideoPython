"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do Peso
Entre 18.5 e 25: Peso Ideal
25 até 30: SobrePeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida
"""
print('*' * 5, 'CALCULO DO IMC', '*' * 5)
peso = float(input('Digite seu Peso em quilos(KG): '))
altura = float(input('Digite sua altura em centímetros: '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Seu IMC é de {:.1f} \nVocê está abaixo do Peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é de {:.1f} \nVocê está com o Peso Ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é de {:.1f} \nVocê está com SobrePeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é de {:.1f} \nVocê está Obeso'.format(imc))
elif imc > 40:
    print('Seu IMC é de {:.1f} \nVocê está com Obesidade Mórbida'.format(imc))