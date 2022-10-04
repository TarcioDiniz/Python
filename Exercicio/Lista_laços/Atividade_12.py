# Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.


repete = 1
while repete == 1:
    try:
        numero_1 = int(input('Digite o 1° número: '))
    except ValueError:
        print('Número invalido. Por favor escolha novamente.')
    else:
        repete = 0

repete = 1
while repete == 1:
    try:
        numero_2 = int(input('Digite o 2° número: '))
    except ValueError:
        print('Número invalido. Por favor escolha novamente.')
    else:
        if numero_2 < numero_1:
            print(f'Escolha um número maior que {numero_1}')
        else:
            repete = 0

print(f'Os número que Estao entre: {numero_1} e {numero_2} é:')
if numero_1 == numero_2 or numero_2 == (numero_1 + 1):
    print('Não existe intervalo. Vazio = {}')

for i in range(numero_1 + 1, numero_2):
    print(f'{i}', end='  ')
