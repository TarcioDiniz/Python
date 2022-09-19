# Faça um programa Python que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

lista_produto = []
for i in range(3):
    numero = float(input(f'produto {i + 1}°, valor: '))
    if numero < 0:
        print('Valor negativo.')
        exit()
    lista_produto.append({f'produto {i + 1}°': numero})

lista_numeros = []
for x in range(3):
    lista_numeros.append(lista_produto[x][f'produto {x + 1}°'])
    lista_numeros.sort()

for verifica in range(3):
    if lista_numeros[0] == lista_produto[verifica][f'produto {verifica + 1}°']:
        produto = str(lista_produto[verifica])
        produto = produto.replace('{', '')
        produto = produto.replace('}', '')
        produto = produto.replace("'", '')
        produto = produto.split(':')
        print(f'Voce deve comprar o {produto[0]} no valor de R${produto[1]}')


