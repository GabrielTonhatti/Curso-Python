n = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n + n2
m = n * n2
d = n / n2
di = n // n2
e = n ** n2
print('A soma é {}, o produto é {}, a divisão é {}'.format(s, m, d), end='. ')
print('Divisão inteira é {} e a potência é {}'.format(di, e))
