# Faça um Programa que leia e armazene 50 números inteiros, mostre a soma, a
# multiplicação e os números.
import random


def multiplication(lista):
    n = 1
    for index in range(len(lista)):
        n *= lista[index]
    return n


numeros = []
for i in range(50):
    numeros.append(random.randint(0, 200))

print(f'Soma: {sum(numeros)}', f'Multiplicação: {multiplication(numeros)}', f'Números: {numeros}', sep='\n')
