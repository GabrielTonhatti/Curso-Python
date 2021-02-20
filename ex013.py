# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Qual o seu salário atual? R$'))
aum = sal * 0.15
print('O seu salário era R${:.2f}, você ganhou 15% de aumento, o seu novo salário é R${:.2f}!'.format(sal, sal + aum))
