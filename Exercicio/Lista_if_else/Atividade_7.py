# Escreva um programa Python que leia três números inteiros e positivos (A, B, C) e
# calcule a seguinte expressão:
while True:
    try:
        a, b, c = input('Informe o valor de A, B, C: ').split(',')
        break
    except ValueError:
        print('Por favor, digite os numeros no formato abaixo:\n "num1, num2, num3"', sep='')

r = eval(f'({a} + {b}) ** 2')
s = eval(f'({b} + {c}) ** 2')
d = eval(f'({r} + {s}) / 2')
print(f'O valor da expressão é: {d}')
