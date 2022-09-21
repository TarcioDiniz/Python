# Faça um Programa Python que converta metros para centímetros.

while True:
    print('Converta metros em centímetros.')
    numero_metros = input('Digite um valor em metros: ')
    try:
        print(eval(f'{numero_metros} * 100'), 'cm', sep='')
        break
    except NameError:
        print('----------------------------')
        print('Por favor, digite um número.')
        print('----------------------------')
        pass
