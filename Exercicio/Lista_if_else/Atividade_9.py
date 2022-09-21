# Faça um Programa Python que peça 2 números inteiros e um número real. Calcule e
# mostre:
# a. o produto do dobro do primeiro com metade do segundo.
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

while True:
    num1 = input('Digite um numero interiro: ')
    if type(eval(num1)) == int:
        break
    else:
        print('----------------------------')
        print('Por favor, digite um número inteiro.')
        print('----------------------------')
while True:
    num2 = input('Digite outro numero inteiro: ')
    if type(eval(num1)) == int:
        break
    else:
        print('----------------------------')
        print('Por favor, digite um número inteiro.')
        print('----------------------------')
while True:
    num3 = input('Digite um numero real: ')
    if type(eval(num3)) == float or int:
        break
    else:
        print('----------------------------')
        print('Por favor, digite um número real.')
        print('----------------------------')


a = eval(f'({num1} * 2) + ({num2} / 2)')
b = eval(f'{num1} * 3 + {num3}')
c = eval(f'{num3} ** 3')

print(f'\nOs número foram: "{num1}, {num2}, {num3}"', sep='')
print(f'O produto do dobro do primeiro com metade do segundo: {a}')
print(f'A soma do triplo do primeiro com o terceiro: {b}')
print(f'O terceiro elevado ao cubo: {c}')








