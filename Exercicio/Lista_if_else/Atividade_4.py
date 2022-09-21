# Uma loja está vendendo seus produtos em 5 (cinco) prestações semjuros. Faça um
# programa Python que receba um valor de uma compra e mostre o valor das
# prestações.

while True:
    print('Saiba os valores da sua prestação.')
    valor_compras = input('Digite o valor total da compra: ')
    print('-----------------------------')

    if eval(valor_compras) < 0:
        print('Você colocou um valor negativo')
        exit()

    try:
        for i in range(5):
            print(f'{i+1}° prestação ', 'R$', eval(f'{valor_compras} / 5'), ' Sem Juros', sep='')
        print('-----------------------------\n', f'Total: R${valor_compras}', sep='')
        print('-----------------------------')
        break

    except NameError:
        print('----------------------------')
        print('Por favor, digite um número.')
        print('----------------------------')
        pass
