# Escreva um programa que calcula o fatorial de um dado número N.
try:
    numero = int(input('Digite um número: '))
except ValueError:
    print('Numero não identificando.')
    exit()
if numero < 0:
    print('Numero negativo, não tem fatorial.')
    exit()

fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(fatorial)
