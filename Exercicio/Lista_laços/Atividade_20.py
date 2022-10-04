# Faça um programa que leia uma quantidade não determinada de números
# positivos. Calcule a quantidade de números pares e ímpares, a média de
# valores pares e a média geral dos números lidos. O número que encerrará a
# leitura será zero.

par = 0
impar = 0
count = 0
soma_geral = 0
repete = 1
while repete == 1:
    try:
        numero = int(input('Informe um número: '))
    except ValueError:
        print('Número não reconhecido. Por favor informe um numero interiro.')
    else:
        if numero == 0:
            repete = 0

        soma_geral += numero
        count += 1

        if numero % 2 == 0:  # numero é par
            par += 1
        else:
            impar += 1

        media_pares = par / count
        media_geral = soma_geral / count

        print(f'Quantidade de números pares: {par}')
        print(f'Quantidade de números impares: {impar}')
        print(f'A média de valores pares: {media_pares}')
        print(f'A média geral dos números lidos: {media_geral}')






