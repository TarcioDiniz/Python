# Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão
# na diagonal secundária.

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
            matrix[i].append(random.randint(0, 99))
    return matrix


matrix_1 = generateMatrix(3, 3)
print_matrix(matrix_1)
sumMatrix = 0
for i in range(len(matrix_1)):
    for j in range(len(matrix_1)):
        if (i + j) == len(matrix_1) - 1:
            sumMatrix += matrix_1[i][j]
            # print(matrix_1[i][j], end=' ')

print('\nSoma da diagonal secundária:', sumMatrix)
