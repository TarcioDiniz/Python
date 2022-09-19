# Faça um Programa Python que leia três números e mostre o maior deles.

lista_numeros = []
for i in range(3):
    try:
        numero = float(input(f'Digite {i + 1}° numero: '))
    except ValueError:
        print('Você digitou uma letra')
        exit()
    lista_numeros.append(numero)
    lista_numeros.sort()

print(f'O maior numero é {lista_numeros[-1]}')

