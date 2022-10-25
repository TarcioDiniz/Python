# Altere o programa anterior, intercalando 3 listas de 10 elementos cada.

import random

lista1 = []
lista2 = []
lista3 = []
recebeElementos = []

for i in range(10):
    lista1.append(random.randint(1, 100))
    lista2.append(chr(random.randint(ord('a'), ord('z'))))
    lista3.append(random.randint(32, 87))

for i in range(10):
    recebeElementos.append(lista1[i])
    recebeElementos.append(lista2[i])
    recebeElementos.append(lista3[i])

print(lista1, f'seu tamanho é {len(lista1)}')
print(lista2, f'seu tamanho é {len(lista2)}')
print(lista3, f'seu tamanho é {len(lista3)}')
print(recebeElementos, f'seu tamanho é {len(recebeElementos)}')
