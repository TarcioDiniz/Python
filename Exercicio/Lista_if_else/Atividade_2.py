# Faça um Programa Python que pergunte quanto você ganha por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

while True:
    print('Calcule seu salario baseado em hora.')
    valor_hora = input('Digite quanto você ganha por hora: ')
    if eval(valor_hora) < 0:
        print('Você colocou um valor negativo')
        exit()
    num_hora = input('Digite o número de horas trabalhadas no mês: ')
    if eval(num_hora) < 0:
        print('Você colocou um valor negativo')
        exit()

    try:
        print('R$', eval(f'{valor_hora} * {num_hora}'), sep='')
        break
    except NameError:
        print('----------------------------')
        print('Por favor, digite um número.')
        print('----------------------------')
        pass




