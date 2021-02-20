# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

d = float(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km o carro rodou? '))
valorD = d * 60
valorKm = km * 0.15
print('O total a pagar é de R${:.2f}'.format(valorD + valorKm))
