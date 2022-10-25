# Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão
# acima da diagonal principal.

"""

[[1, 2, 3],
 [1, 2, 3],
 [1, 2, 3]]

soma 2 + 3

"""

matriz = [[1, 10, 3],
          [1, 2, 11],
          [1, 2, 3]]

sumMatrix = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j > i:
            try:
                sumMatrix += matriz[i][j]
                #print(matriz[i][j])
            except IndexError:
                pass

print(sumMatrix)
