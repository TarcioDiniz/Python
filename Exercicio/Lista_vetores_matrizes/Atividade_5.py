# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
# numa lista a média de cada aluno, imprima o número de alunos com média
# maior ou igual a 7.0.
import random

alunos = []
medias = []
for i in range(10):
    alunos.append([])
    for j in range(4):
        alunos[i].append(random.randint(0, 10))


for i in range(len(alunos)):
    medias.append(sum(alunos[i]) / 4)

dicionary = []

for i in range(10):
    dicionary.append({
        'Aluno': f'{i + 1}° Aluno',
        'Notas': alunos[i],
        'Media': medias[i]
    })

count = 0
for i in range(10):
    if dicionary[i]['Media'] >= 7:
        count += 1
        print(dicionary[i]["Aluno"],
              f'Notas: {dicionary[i]["Notas"]}',
              f'Media: {dicionary[i]["Media"]}', sep='\n')
if count == 0:
    print('Ninguem conseguiu passar.')