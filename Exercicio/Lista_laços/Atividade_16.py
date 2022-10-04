# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
# programa que leia um conjunto indeterminado de temperaturas, e informe ao
# final a menor e a maior temperatura informada, bem como a média das
# temperaturas.

RED = "\033[1;31m"
BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"

repete = 1
while repete == 1:
    try:
        qnt_temp = int(input('Informe quantas temperaturas você que colocar: '))
    except ValueError:
        print(f'{RED}Número invalido, por favor repita.{RESET}')
        pass
    else:
        repete = 0

repete = 1
while repete == 1:
    try:
        temperatura = float(input('Informe a 1° temperatura: '))
    except ValueError:
        print(f'{RED}Número invalido, por favor repita.{RESET}')
        pass
    else:
        repete = 0

maior = temperatura
menor = temperatura
soma = temperatura


for i in range(1, qnt_temp):
    repete = 1
    while repete == 1:
        try:
            temperatura = float(input(f'Informe a {i + 1}° temperatura: '))
        except ValueError:
            print(f'{RED}Número invalido, por favor repita.{RESET}')
            pass
        else:
            repete = 0

    if temperatura > maior:

        maior = temperatura

    elif temperatura < menor:
        menor = temperatura

    soma += temperatura

media = soma / qnt_temp

print(f'\nO menor número é: {menor}',
      f'O maior número é: {maior}',
      f'A media das temperaturas são: {media}', sep='\n')
