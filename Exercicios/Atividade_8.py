# Escrever um programa Python que leia o nome de um vendedor, o seu salário fixo e o
# total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor
# ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário
# fixo e salário no final do mês

nome_vendedor = input('Nome do vendedor: ').capitalize()
while True:
    salario_vendedor = input(f'Salário do vendedor {nome_vendedor}: ')
    if salario_vendedor.isdigit():
        break
    else:
        print('----------------------------')
        print('Por favor, digite um número.')
        print('----------------------------')
while True:
    total_vendas_vendedor = input(f'Total de vendas do vendedor {nome_vendedor} no mês: ')
    if total_vendas_vendedor.isdigit():
        break
    else:
        print('----------------------------')
        print('Por favor, digite um número.')
        print('----------------------------')
print('\n-----------------------------', sep='')
print('Seu salário no final:')
print('R$', eval(f'{salario_vendedor} * (15/100) + {salario_vendedor}'), sep='')
print('-----------------------------')



