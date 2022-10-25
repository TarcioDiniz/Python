# Faça um Programa que leia duas listas com 10 elementos cada. Gere uma
# terceira lista de 20 elementos, cujos valores deverão ser compostos pelos
# elementos intercalados das duas outras listas.

import random

lista1 = []
lista2 = []
recebeElementos = []

for i in range(10):
    lista1.append(random.randint(1, 100))
    lista2.append(random.randint(50, 200))

for i in range(10):
    recebeElementos.append(lista1[i])
    recebeElementos.append(lista2[i])

print(lista1, f'seu tamanho é {len(lista1)}')
print(lista2, f'seu tamanho é {len(lista2)}')
print(recebeElementos, f'seu tamanho é {len(recebeElementos)}')
