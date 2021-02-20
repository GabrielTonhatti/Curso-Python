'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
-Abaixo de 18.5:Abaixo do peso
-Entre 18.5 e 25:Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40:Obesidade mórbida'''

altura = float(input('Qual sua altura? \n'))
peso = float(input('Qual o seu peso? \n'))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está \033[33mabaixo do peso\033[m!')
elif imc >= 18.5 and imc < 25:
    print('Você está no \033[32mpeso ideal\033[m!')
elif imc >= 25 and imc <= 30:
    print('Você está com \033[33msobrepeso\033[m!')
elif imc > 30 and imc <= 40:
    print('Você está com \033[31mobesidade\033[m!')
else:
    print('Você está com \033[31mobesidade mórbida\033[m!!')
