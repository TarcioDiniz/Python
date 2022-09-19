# Faça um Programa Python para um caixa eletrônico. O programa deverá perguntar ao
# usuário a valor do saque e depois informar quantas notas de cada valor serão
# fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é
# de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a
# quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
# uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


def _valor_():
    while True:
        try:
            valor_saque = int(input('Informe o valor do saque: '))
            if 10 <= valor_saque <= 600:
                break
            else:
                print('Por favor, digite um valor entre 10 e 600')
                pass
        except ValueError:
            print('-' * 28, '\nPor favor, digite um número.\n', '-' * 28, sep='')
            pass

    return valor_saque


def analisa_notas(valor_total):
    lista_notas = [1, 5, 10, 50, 100]
    notas_saque = []
    count_notas = 0
    for i in range(1, len(lista_notas) + 1):
        while True:
            count_notas += lista_notas[-i]
            notas_saque.append(lista_notas[-i])
            if count_notas >= valor_total:
                if count_notas - valor_total > 0:
                    count_notas = count_notas - lista_notas[-i]
                    notas_saque.pop(-1)
                break
        valor_total = valor_total - count_notas
        count_notas = 0
    print('\nVocê receberá:')
    for _print_ in range(len(lista_notas)):
        print(f'{notas_saque.count(lista_notas[_print_])} notas de {lista_notas[_print_]}')


valor = _valor_()
analisa_notas(valor)
