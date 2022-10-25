# Faça um programa que leia um número indeterminado de valores,
# correspondentes a notas, encerrando a entrada de dados quando for informado
# um valor igual a -1 (que não deve ser armazenado). Após esta entrada de
# dados, faça:
# a. Mostre a quantidade de valores que foram lidos;
# b. Exiba todos os valores na ordem em que foram informados
# c. Exiba todos os valores na ordem inversa à que foram informados
# d. Calcule e mostre a soma dos valores;
# e. Calcule e mostre a média dos valores;
# f. Calcule e mostre a quantidade de valores acima da média calculada;
# g. Calcule e mostre a quantidade de valores abaixo de sete;
# h. Encerre o programa com uma mensagem.

def aboveAverage(array):
    aboveAverage_list = []
    average = sum(array) / len(array)
    for i in range(len(array)):
        if array[i] > average:
            aboveAverage_list.append(array[i])

    return len(aboveAverage_list)


def belowAverage(array):
    belowAverage_list = []
    for i in range(len(array)):
        if array[i] < 7:
            belowAverage_list.append(array[i])

    return len(belowAverage_list)


notasValue = [float(input('Informe a 1 nota do aluno: '))]

while notasValue[-1] > -1:
    print(f'\nQuantidade de números lidos: {len(notasValue)}',
          f'Valores na ordem em que foram informados: {notasValue}',
          f'Valores na ordem inversa à que foram informados: {list(reversed(notasValue))}',
          f'Soma dos valores: {sum(notasValue)}',
          f'Média dos valores: {(sum(notasValue)) / len(notasValue)}',
          f'Quantidade de valores acima da média calculada: {aboveAverage(notasValue)}',
          f'Quantidade de valores abaixo de sete: {belowAverage(notasValue)}', sep='\n')

    notasValue.append(float(input(f'Informe a {len(notasValue) + 1} nota do aluno: ')))

print('Encerrado')
