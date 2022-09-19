# Faça um programa Python para a leitura de duas notas parciais de um aluno. O
# programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez


nota_1 = float(input('Digite a primeira nota: '))
if nota_1 < 0 or nota_1 > 10:
    print('Desculpe, digite uma nota de 0 a 10.')
    exit()


nota_2 = float(input('Digite a segunda nota: '))
if nota_2 < 0 or nota_2 > 10:
    print('Desculpe, digite uma nota de 0 a 10.')
    exit()

media = (nota_1 + nota_2) / 2

if media == 10:
    print('Aprovado com Distinção')
else:
    if media >= 7:
        print('Aprovado')
    else:
        if media < 7:
            print('Reprovado')


