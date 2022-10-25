# Faça um Programa que leia 40 notas, mostre as notas e a média na tela

import random

notas = []
for i in range(40):
    notas.append(random.randint(1, 10))

media = sum(notas) / len(notas)

print(f'Notas: {notas}\nMédia: {media}')
