# Faça um Programa que leia 20 números inteiros e armazene-os numa lista.
# Armazene os números pares na lista PAR e os números IMPARES na lista
# impar. Imprima as três listas.
import random

numero = []
par = []
impar = []

for i in range(20):
    numero.append(random.randint(0, 100))

for j in range(20):
    if numero[j] % 2 == 0:
        par.append(numero[j])
    else:
        impar.append(numero[j])

print(f'Todos os números: {numero}', f'Impares: {impar}', f'Pares: {par}', sep='\n')
