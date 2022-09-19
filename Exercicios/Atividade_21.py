# Faça um Programa Python que peça os 3 lados de um triângulo. O programa deverá
# informar se os valores podem ser um triângulo. Indique, caso os lados formem um
# triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

# Dicas: Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
# que o terceiro; Triângulo Equilátero: três lados iguais; Triângulo isósceles: quaisquer dois
# lados iguais; Triângulo Escaleno: três lados diferentes;

_lados = []

for i in range(3):
    try:
        _lados.append(float(input(f'Lado {i + 1}: ')))
    except ValueError:
        print('Número não reconhecido.')
        exit()

a = _lados[0]
b = _lados[1]
c = _lados[2]

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')
elif (a == b) and (a == c):
    print('Triângulo Equilatero')
elif (a == b) or (a == c) or (b == c):
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')
