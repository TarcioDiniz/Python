# Faça um Programa que leia 5 números inteiros, armazene-os em uma lista.

lista = []
for i in range(5):
    lista.append(int(input(f'Digite o {i+1}° inteiro: ')))

print(f'Os 5 número inteiros foram:\n{lista}')
