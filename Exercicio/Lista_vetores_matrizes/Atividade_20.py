# Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma
# busca desse valor na matriz e, ao final, escrever a localizacão (linha e coluna)
# ou uma mensagem de “não encontrado”.

import random


def generateMatrix(line, column):
    matrix = []
    for i in range(line):
        matrix.append([])
        for j in range(column):
            matrix[i].append(random.randint(0, 99))
    return matrix


matrix_1 = generateMatrix(5, 5)
# print(matrix_1)
numerateSearch = int(input('Informe o valor que queria procurar: '))
found = True
for i in range(len(matrix_1)):
    for j in range(len(matrix_1)):
        if matrix_1[i][j] == numerateSearch:
            print(f'Foi encontrado! Sua localização matriz[{i}][{j}]')
            found = False
if found:
    print('Não encontrado')
