# Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os
# demais elementos. Escreva ao final a matriz obtida.7

# Create new matriz
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


matriz = []
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(0)

    # write in main diagonal
    matriz[i][i] = 1

print_matrix(matriz)