# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando
# dados sobre o salário e número de filhos. A prefeitura deseja saber:
# a) Média do salário da população;
# b) Média do número de filhos;
# c) Maior salário;
# d) Percentual de pessoas com salário até R$250,00.
# Desenvolver um programa para calcular e escrever o que foi pedido nos itens
# a, b, c e d. O final da leitura de dados se dará com a entrada de um salário
# negativo.

salario_250 = 0
verifica = 1
while verifica == 1:
    try:
        salario = float(input('Informe seu salario: '))
    except ValueError:
        print('Número não identificado')
    else:
        if salario < 0:
            verifica = 0
            media_salario = 0
            media_filhos = 0
            salario_maior = 0
            percentual_250 = 0

        else:
            if salario <= 250:
                salario_250 += 1

            verifica = 1
            while verifica == 1:
                try:
                    filhos = int(input('Informe o número de filhos: '))
                except ValueError:
                    print('Numero não identificado.')
                else:
                    if filhos < 0:
                        print('Se deseja encerrar o programa, coloque valores negativos em salario. Por favor, '
                              'repita a quantidade de números de filhos com um inteiro positivo.')
                    else:
                        verifica = 0

            repete = 1
            habitante = 1

            salario_maior = salario
            salario_menor = salario

            soma_filhos = filhos
            soma_salario = salario

            while repete == 1:
                salario = float(input('Informe seu salario: '))

                if salario <= 250:
                    salario_250 += 1

                soma_salario += salario

                if salario < 0:
                    repete = 0

                else:

                    verifica = 1
                    while verifica == 1:
                        try:
                            filhos = int(input('Informe o número de filhos: '))
                        except ValueError:
                            print('Numero não identificad.')
                        else:
                            if filhos < 0:
                                print('Se deseja encerrar o programa, coloque valores negativos em salario. Por favor, '
                                      'repita a quantidade de números de filhos com um inteiro positivo.')
                            else:
                                verifica = 0

                    soma_filhos += filhos

                    if salario > salario_maior:
                        salario_maior = salario

                    elif salario < salario_menor:
                        salario_menor = salario

                    habitante += 1

                    media_salario = soma_salario / habitante

                    media_filhos = soma_filhos / habitante

                    percentual_250 = (salario_250 * 100) / habitante

try:
    print("Média do salário da população: {:.2f}".format(media_salario))
    print(f"Média do número de filhos: {media_filhos}")
    print("Maior salário: ", salario_maior)
    print("Percentual de pessoas com salário até R$250,00: {:.2f}%".format(percentual_250))
except NameError:
    print("Média do salário da população: {:.2f}".format(salario_maior))
    print(f"Média do número de filhos: {filhos}")
    print("Maior salário: ", salario_maior)
    print("Percentual de pessoas com salário até R$250,00: Undefined ")
