# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares
# ela pode comprar. Considere US$1,00 = R$3,27

money = float(input('Quanto de dinheiro você? R$'))
print('Com R${} você pode comprar US${:.2f}!'.format(money, money / 3.27))
