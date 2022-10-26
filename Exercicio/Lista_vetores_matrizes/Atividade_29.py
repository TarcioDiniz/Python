# Uma loja vende sapatos femininos de três marcas: A, B e C e tamanhos de 35 a
# 40. O gerente da loja lhe solicitou um programa para manipular dados referentes
# ao estoque desta loja. Desta forma, você deve ler para cada marca de sapato e
# numeração a sua respectiva quantidade e informar a numeração que possui a
# maior quantidade em estoque. A seguir é apresentado um exemplo de tabela com
# os dados do estoque.


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


def _matrixT(matrix):
    matrizT = []
    for i in range(len(matrix[0])):
        matrizT.append([0] * len(matrix))

    for i in range(len(matrizT)):
        for j in range(len(matrizT[0])):
            matrizT[i][j] = matrix[j][i]

    return matrizT


products = generateMatrix(3, 6)
tamanhos = [35, 36, 37, 38, 39, 40]

print_matrix(products)

# sumTamanho = list(map(list, zip(*products)))
sumTamanho = _matrixT(products)
listaMaior = []
for i in range(len(sumTamanho)):
    listaMaior.append(sum(sumTamanho[i]))

maiorQuant = max(listaMaior)

for i in range(len(sumTamanho)):
    if (sum(sumTamanho[i])) == maiorQuant:
        print(f'\nTamanho {tamanhos[sumTamanho.index(sumTamanho[i])]} tem a maior quatidade no estoque, '
              f'com: {maiorQuant} unidades')
