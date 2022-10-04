# Sendo H = 1/1 + 1/2 + 1/3 + 1/4 + ... + 1/N. Faça um programa para gerar e
# mostrar o número H. O número N será fornecido como entrada.

numero = int(input('Infome o numero de vezes que você quer somar: '))
if numero < 0:
    print('numero negativo??')
    exit()

h = 0
for i in range(1, numero + 1):
    h += 1/i

print(h)
