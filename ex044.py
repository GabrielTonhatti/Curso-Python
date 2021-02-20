'''Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:

-À vista dinheiro/cheque: 10% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros.'''

produto = float(input('Digite o valor do produto: \nR$'))
print('1 - dinheiro/cheque:')
print('2 - para cartão:')
pagamento = int(input())

if pagamento == 1:
    desconto = produto - (produto * 0.1)
    pago = float(input('Digite o valor dado em dinheiro/cheque: \nR$'))
    troco = pago - desconto
    print('O valor final do produto vai ser de R${:.2f}, com 10% de desconto, o troco é de R${:.2f}!'.format(desconto, troco))
elif pagamento == 2:
    parcela = (int(input('Digite em quantas vezes deseja parcelar a comprar: \n')))
    if parcela <= 2 and parcela > 0:
        parcelamento = produto / parcela
        print('O valor do produto é de R${:.2f}, em {}X de R${:.2f} sem juros!'.format(produto, parcela, parcelamento))
    elif parcela >= 3:
        juros = produto + (produto * 0.2)
        parcelamento = juros / parcela
        print('O valor final do produto é de R${:.2f}, em {}X de R${:.2f}, com 20% de juros!'.format(produto, parcela, parcelamento))
else:
    print('Forma de pagamento ínvalida!')