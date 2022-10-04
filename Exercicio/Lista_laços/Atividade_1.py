# Escreva um programa que calcula a média de 30 alunos e informa a situação
# (reprovado, aprovado ou recuperação).

# reprovado < 5
# recuperação 5 <= x < 7
# aprovado >= 7

RED = "\033[1;31m"
BLUE = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"

print(f'{BOLD}Aprovado ou Reprovado{RESET}')
print('-' * 54)

for i in range(30):
    try:
        nota_1 = float(input(f'Informe a primeira nota do {i + 1}° aluno: '))
    except ValueError:
        print(f'{RED}Valor não reconhecido{RESET}')
        nota_1 = 0
    try:
        nota_2 = float(input(f'Informe a segunda nota do {i + 1}° aluno: '))
    except ValueError:
        print(f'{RED}Valor não reconhecido{RESET}')
        nota_2 = 0

    if nota_1 > 10 or nota_2 > 10:
        print(f'Querendo trapacear?? {RED}NOTA ZERO{RESET}')
        nota_1 = 0
        nota_2 = 0
    else:
        if nota_1 < 0 or nota_2 < 0:
            print(f'Nota Negativa??? Por conta disso sua Média será {RED}ZERO{RESET}')
            nota_1 = 0
            nota_2 = 0

    try:
        if nota_1 + nota_2 == 0:
            media = 0
        else:
            media = (nota_1 + nota_2) / 2

        if media < 5:
            situacao_aluno = f'foi {RED}REPROVADO'
        else:
            if 5 <= media < 7:
                situacao_aluno = f'estar em {BLUE}RECUPERAÇÃO'
            else:
                if media >= 7:
                    situacao_aluno = f'foi {GREEN}APROVADO'

        print(f'O aluno {i + 1}° {situacao_aluno} {RESET}e sua média foi %.2f' % media)
        print('-' * 54)
    except NameError:
        pass