# Escreva um programa que transforme uma matriz 4x4 numa matriz triangular
# inferior, ou seja, atribuindo zero a todos os elementos acima da diagonal
# principal. Imprima a matriz original e a matriz transformada.

import random


def print_matrix(matrix):
    def maxNumberMatrix(matrix):
        maxNubers = []
        for i in range(len(matrix)):
            maxNubers.append(max(matrix[i]))

        return len(str(max(maxNubers))) + 1

    matriz = matrix
    indentation = maxNumberMatrix(matriz)
    matrizString = []

    for i in range(len(matriz)):
        matrizString.append([])
        for j in range(len(matriz[0])):
            matrizString[i].append(str(matriz[i][j]))

    for i in range(len(matrizString)):
        for j in range(len(matrizString[0])):
            if i == j:
                print(f'{matrizString[i][j]:>{indentation}}', end=' ')
            else:
                print(f'{matrizString[i][j]:>{indentation}}', end=' ')
        print()


def generateMatrix(line, column):
    matrix = []
    for i in range(line):
        matrix.append([])
        for j in range(column):
            matrix[i].append(random.randint(1, 100))
    return matrix


matriz = generateMatrix(4, 4)
print('Antes')
print_matrix(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j > i:
            try:
                matriz[i][j] = 0
                # print(matriz[i][j])
            except IndexError:
                pass
print('\nDepois')
print_matrix(matriz)
