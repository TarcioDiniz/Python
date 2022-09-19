# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
# tabela abaixo:
# • Média de Aproveitamento Conceito
# • Entre 9.0 e 10.0 A
# • Entre 7.5 e 9.0 B
# • Entre 6.0 e 7.5 C
# • Entre 4.0 e 6.0 D
# • Entre 4.0 e zero E
# O programa Python deve mostrar na tela as notas, a média, o conceito correspondente
# e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
# conceito for D ou E.


notas = []
for i in range(2):
    try:
        notas.append(float(input(f'Nota {i + 1}: ')))
    except ValueError:
        print('Número não reconhecido.')
        exit()
    if notas[-1] < 0:
        print('Valor negativo.')
        exit()
    if 0 <= notas[-1] <= 10:
        pass
    else:
        print('Digite a nota no valor de 0 a 10.')

media = sum(notas)/len(notas)

if 9 <= media <= 10:
    print('Aprovado com A')
else:
    if 7.5 <= media < 9:
        print('Aprovado com B')
    else:
        if 6 <= media < 7.5:
            print('Aprovado com C')
        else:
            if 4 <= media < 6:
                print('Reprovado com D')
            else:
                if 0 <= media < 4:
                    print('Reprovado com E')