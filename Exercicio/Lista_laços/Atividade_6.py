# Faça um programa para calcular um valor A elevado a um expoente B. Os
# valores A e B deverão ser lidos. Não usar A** B e sim uma estrutura de
# repetição.


valor_A = int(input('Informe o valor de A: '))
valor_B = int(input('Informe o valor de B: '))

total = 1

if valor_B < 0:
    for i in range(abs(valor_B)):
        total *= 1/valor_A

for i in range(valor_B):
    total *= valor_A

print(total)

