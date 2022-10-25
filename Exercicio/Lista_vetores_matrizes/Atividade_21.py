# Leia duas matrizes 4x4 e escreva uma terceira com os maiores valores de
# cada posição das matrizes lidas
import random


def generateMatrix(line, column):
    matrix = []
    for i in range(line):
        matrix.append([])
        for j in range(column):
            matrix[i].append(random.randint(0, 99))
    return matrix


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


matrix_1 = generateMatrix(4, 4)
matrix_2 = generateMatrix(4, 4)
matrix_3 = generateMatrix(4, 4)

for i in range(len(matrix_1)):
    for j in range(len(matrix_1)):
        if matrix_1[i][j] > matrix_2[i][j]:
            matrix_3[i][j] = matrix_1[i][j]
        else:
            matrix_3[i][j] = matrix_2[i][j]

print('1° Matriz:')
print_matrix(matrix_1)
print('\n2° Matriz:')
print_matrix(matrix_2)
print('\n3° Matriz:')
print_matrix(matrix_3)
