# Faça um Programa que leia 10 números reais e mostre-os na ordem inversa.
lista = []
for i in range(10):
    lista.append(float(input(f'Digite o {i+1}° real: ')))

lista = list(reversed(lista))

print(f'A lista invertida é {lista}')