# Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela
# possui.

import random


def generateMatrix(line, column):
    matrix = []
    for i in range(line):
        matrix.append([])
        for j in range(column):
            matrix[i].append(random.randint(0, 99))
    return matrix


matrix_1 = generateMatrix(4, 4)
count = 0
for i in range(4):
    for j in range(4):
        if matrix_1[i][j] > 10:
            count +=1
print(f'Ela possui {count} maiores que 10.')

