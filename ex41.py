'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Até 20 anos: SÊNIOR
-Acima: MASTER'''
from datetime import date

ano = date.today().year
nascimento = int(input('Digite o ano de nascimento do atleta: \n'))
idade = ano - nascimento

if idade <= 9:
    print('Atleta Mirim!')
elif idade > 9 and idade <= 14:
    print('Alteta Infaltil!')
elif idade > 14 and idade <= 19:
    print('Atleta Junior!')
elif idade > 19 and idade <= 20:
    print('Atleta Sênior!')
else:
    print('Atleta Master!')
