# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Digite o preço do produto: R$'))
desc = preco * 0.05
print('O preço do produto é R${:.2f}, na liquidação ele ficara com 5% de desconto,'.format(preco), end=' ')
print('ira sair por R${:.2f}!'.format(preco - desc))
