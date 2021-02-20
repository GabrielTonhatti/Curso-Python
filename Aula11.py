print('\033[7;33;44mOlá, Mundo!\033[m')

a = 5
b = 3

print()
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

nome = 'Gabriel'
cores = {'limpa':'\033[m', 
        'azul':'\033[34m', 
        'amarelo':'\033[33m', 
        'pretoebranco':'\033[7;30m'}
print('Muito prazer em te conhecer {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))