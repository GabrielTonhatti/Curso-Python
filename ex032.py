'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''
from datetime import date
print('Digite 0 caso queira analisar o ano atual.')
ano = int(input('Digite um ano qualquer que deseja saber se é bissexto ou não: \n'))

if ano == 0:
    ano = date.today().year
    
bissexto = ano % 4
bissexto2 = ano % 100
bissexto3 = ano % 400

if bissexto == 0:
    if bissexto2 == 0:
        if bissexto3 == 0:
            anob = 1
        else:
            anob = 0
    elif bissexto2 != 0:
        anob = 1
    else:
        anob = 0
elif bissexto2 != 0 and bissexto3 == 0:
    anob = 1
else:
    anob = 0

if anob == 1:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))