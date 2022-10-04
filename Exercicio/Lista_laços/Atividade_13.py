# Faça um programa que peça um número inteiro e determine se ele é ou não
# um número primo. Um número primo é aquele que é divisível somente por ele
# mesmo e por 1.


numero = int(input("Verificar se o numero é primo: "))
count = 0

for i in range(2, numero):
    if numero % i == 0:
        count += 1

if count == 0:
    print("É primo")
else:
    print('Não é primo')
