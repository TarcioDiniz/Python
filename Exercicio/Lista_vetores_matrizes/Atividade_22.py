# . Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da
# forma:
# a. A[i][j] = 2i + 7j −2 se i < j;
# b. A[i][j] = 3i2
#  −1 se i = j;
# c. A[i][j] = 4i3
#  −5j2
#  + 1 se i > j.
# import numpy

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


matrx_1 = generateMatrix(10, 10)
print(matrx_1)

for i in range(len(matrx_1)):
    for j in range(len(matrx_1)):
        if i < j:
            matrx_1[i][j] = (2 * i) + (7 * j) - 2
        else:
            if i == j:
                matrx_1[i][j] = (3 * (i ** 2)) - 1
            else:
                if i > j:
                    matrx_1[i][j] = (4 * (i ** 3)) - (5 * (j ** 2)) - 1

# print(numpy.matrix(matrx_1))
print_matrix(matrx_1)
