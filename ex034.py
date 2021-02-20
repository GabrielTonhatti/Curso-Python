'''Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.
Para salário superiores a R$ 1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''

sal = float(input('Qual o seu salário atual? \nR$'))

if sal > 1250:
    aumento = sal + (sal * 0.10)
    print('Você ganhou um aumento de 10%, o seu novo salário é R${:.2f}!'.format(aumento))
else:
    aumento = sal + (sal * 0.15)
    print('Você ganhou um aumento de 15%, o seu novo salário é R${:.2f}!'.format(aumento))
