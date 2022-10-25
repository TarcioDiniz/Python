# Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas e
# armazene os nomes lidos em uma lista. Após isto, o algoritmo deve permitir a
# leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem
# ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados
# na lista), ou NÃO ACHEI caso contrário.


# maneira usando uma API do IBGE que capitura nomes aleatorios.

'''import random
import requests

dicionaryIBGE = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking').json()
data = dicionaryIBGE[0]['res']
nomes = []

for i in range(10):
    nomes.append(data[random.randint(0, 19)]['nome'])

if input('Pesquise pelo nome: ').upper().replace(' ', '') in nomes:
    print('ACHEI')
else:
    print('NÃO ACHEI')'''

nomes = []
for i in range(10):
    nomes.append(input(f'Acrecentar pessoa {i + 1}: ').upper().replace(' ', ''))

if input('Pesquise pelo nome: ').upper().replace(' ', '') in nomes:
    print('ACHEI')
else:
    print('NÃO ACHEI')
