# Faça um programa Python que receba o preço de custo de um produto e mostre o
# valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com
# um percentual informado pelo usuário.

while True:
    preco_custo = input('Digite o preço de custo do produto: ')
    if preco_custo.isdigit():
        break
    else:
        try:
            if eval(preco_custo) < 0:
                print('-' * 30, '\nVocê colocou um valor negativo\n', '-' * 30, sep='')
        except NameError:
            print('-' * 28, '\nPor favor, digite um número.\n', '-' * 28, sep='')

while True:
    aumento = input('Digite o valor do aumento em porcentagem: ')
    if aumento.isdigit():
        break
    else:
        print('----------------------------')
        print('Por favor, digite um número.')
        print('----------------------------')

print('Valor total: ', 'R$', eval(f'{preco_custo} * ({aumento} / 100) + {preco_custo}'), sep='')
