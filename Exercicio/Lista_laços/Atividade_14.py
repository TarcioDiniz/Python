# Faça um programa que peça para n pessoas a sua idade, ao final o programa
# devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e
# maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
# média calculada.

n = int(input('Informe o número de pessoas que você quer calcular a média: '))
soma_idade = 0
i = -1
while i + 2 <= n:
    if i == n:
        n = -1
    i += 1
    idade = int(input(f'Informe a idade da {i + 1}° pessoa: '))
    if idade < 0:
        print('Idade negativa?? \nPor favor, digite uma idade correta.')
        i = i - 1
        idade = 0

    soma_idade += idade

media = soma_idade / n

if 0 < media < 25:
    print("A média de idades é de uma turma jovem.")
else:
    if 25 < media < 60:
        print("A média de idades é de uma turma adulta.")
    else:
        if media > 60:
            print("A média de idades é de uma turma")
