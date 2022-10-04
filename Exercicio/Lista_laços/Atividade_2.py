# Escreva um programa que leia 10 números e informe o maior e o menor
# número.

RED = "\033[1;31m"
BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"

repete = 1
while repete == 1:
    try:
        num = float(input(f'Digite o valor 1° número: '))
    except ValueError:
        print(f'{RED}Número invalido, por favor repita.{RESET}')
        pass
    else:
        repete = 0

maior = num
menor = num

for i in range(1, 10):
    repete = 1
    while repete == 1:
        try:
            num = float(input(f'Digite o valor {i + 1}° número: '))
        except ValueError:
            print(f'{RED}Número invalido, por favor repita.{RESET}')
            pass
        else:
            repete = 0

    if num > maior:

        maior = num

    elif num < menor:
        menor = num

print(f'{GREEN}Menor:{RESET} {menor}')
print(f'{GREEN}Maior:{RESET} {maior}')