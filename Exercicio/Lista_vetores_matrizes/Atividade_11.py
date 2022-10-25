# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que
# determine quantos alunos com mais de 13 anos possuem altura inferior à
# média de altura desses alunos.
import random
idade = []
altura = []
dicionary = []
for i in range(30):
    idade.append(random.randint(5, 85))
    altura.append(round(random.uniform(1.00, 2.00), 2))

for i in range(len(idade)):
    dicionary.append({
        'Idade': idade[i],
        'Altura': altura[i]
    })


for i in range(len(dicionary)):
    if dicionary[i]['Idade'] >= 13:
        if dicionary[i]['Altura'] < (sum(altura) / len(altura)):
            print(f'Pessoa: {i}', f'Idade: {dicionary[i]["Idade"]}', f'Altura: {dicionary[i]["Altura"]}')