# Faça um Programa que peça a idade e a altura de 10 pessoas, armazene cada
# informação na sua respectiva lista. Imprima a idade da pessoa que possui
# maior altura
import random

pessoas = []
altura = []
for i in range(10):
    alturaChoice = round(random.uniform(1.00, 2.00), 2)
    altura.append(alturaChoice)
    pessoas.append({
        'idade': random.randint(7, 70),
        'Altura': alturaChoice
    })

for i in range(len(pessoas)):
    if pessoas[i]['Altura'] == max(altura):
        print(f'Pessoa: {i + 1}', f'Idade: {pessoas[i]["idade"]}', f'Altura: {pessoas[i]["Altura"]}', '\n', sep='\n')
