'''Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai pergunta o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''
casa = float(input('Qual o valor da casa que deseja comprar? \nR$'))
salario = float(input('Qual o seu salário? \nR$'))
num_par = int(input('Em quantos anos deseja pagar o empréstimo? \n'))
valor_par = casa / (num_par * 12)

if valor_par < (salario * 0.3):
    print('Empréstimo \033[32mAPROVADO\033[m!')
    print('O valor da parcela vai ser de R${:.2f} em {} anos, solicitado por você!'.format(valor_par, num_par))
else:
    print('Empréstimo \033[31mNEGADO\033[m!')
    print('O valor da parcela ultrapassa os 30% do seu salário, no valor de R${:.2f} em {} anos, por isso não podemos aceitar o valor do empréstimo'.format(valor_par, num_par))