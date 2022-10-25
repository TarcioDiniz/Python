# Faça um programa que leia duas matrizes 2 x 2 com valores reais. Ofereça ao
# usuário um menu de opções:
# (a) somar as duas matrizes
# (b) subtrair a primeira matriz da segunda
# (c) adicionar uma constante as duas matrizes
# (d) imprimir as matrizes.
# Nas duas primeiras opções uma terceira matriz deve ser criada.
# Na terceira opção o valor da constante deve ser lido e o resultado da adição da
# constante deve ser armazenado na própria matriz.

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


def sumMatrizA_B(matrix1, matrix2):
    matrix = []
    for i in range(len(matrix1)):
        matrix.append([])
        for j in range(len(matrix1)):
            matrix[i].append(matrix1[i][j] + matrix2[i][j])
    return matrix


def subtractMatrixA_B(matrix1, matrix2):
    matrix = []
    for i in range(len(matrix1)):
        matrix.append([])
        for j in range(len(matrix1)):
            matrix[i].append(matrix1[i][j] - matrix2[i][j])
    return matrix


def postConstantInMatrix(const, *args):
    # print(args[0], len(args))
    matrix = []
    for repeat in range(len(args)):
        matrix.append([])
        for i in range(len(args[repeat])):
            matrix[repeat].append([])
            for j in range(len(args[repeat])):
                matrix[repeat][i].append(args[repeat][i][j] * const)
    return matrix


matrix_1 = generateMatrix(2, 2)
matrix_2 = generateMatrix(2, 2)


options = ['(a) somar as duas matrizes.', '(b) subtrair a primeira matriz da segunda.',
           '(c) adicionar uma constante as duas matrizes.', '(d) imprimir as matrizes.']

for i in range(len(options)):
    print(options[i])
choice = input('Escolha uma opção: ').upper()
if choice == 'A':
    print_matrix(sumMatrizA_B(matrix_1, matrix_2))
else:
    if choice == 'B':
        print_matrix(subtractMatrixA_B(matrix_1, matrix_2))
    else:
        if choice == 'C':
            const = float(input('Informe o valor da constante: '))
            matrixAll = postConstantInMatrix(const, matrix_1, matrix_2)
            print(f'Matriz 1 * {const}')
            print_matrix(matrixAll[0])
            print(f'Matriz 2 * {const}')
            print_matrix(matrixAll[1])

        else:
            if choice == 'D':
                print('matriz 1')
                print_matrix(matrix_1)
                print('matriz 2')
                print_matrix(matrix_2)
            else:
                print('Escolha errada. Tente novamente.')
