# Uma grande firma deseja saber qual é o empregado mais recente e qual é o
# mais antigo. Desenvolver um programa para ler um número indeterminado de
# informações contendo o número do empregado e o número de meses de
# trabalho deste empregado e
# imprimir o mais recente e o mais antigo.
# Obs.: A
# última informação contém os dois números iguais a zero. Não existem dois
# empregados admitidos no mesmo mês.

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

count = 1
while count == 1:
    try:
        id_empregado = int(input('Informe o ID do empregado: '))
    except ValueError:
        print(f'{RED}ID precisa ser um numero inteiro positivo.{RESET}')
        pass
    else:
        count = 0

count = 1
while count == 1:
    try:
        meses_trabalhados = int(input('Informe a quantidade de meses trabalhados: '))
    except ValueError:
        print(f'{RED}O MES precisa ser um numero inteiro positivo.{RESET}')
        pass
    else:
        count = 0

recente = meses_trabalhados
id_recente = id_empregado

antigo = meses_trabalhados
id_antigo = id_empregado

id_list = [id_empregado]
meses_lista = [meses_trabalhados]

repete = 1
while repete == 1:
    count = 1
    while count == 1:
        try:
            id_empregado = int(input('\nInforme o ID do empregado: '))
        except ValueError:
            print(f'{RED}ID precisa ser um numero inteiro positivo.{RESET}')
            pass
        else:
            if id_empregado in id_list:
                print(f'{RED}Este id ja possui, por favor tente outro.{RESET}')
                pass
            else:
                count = 0

    count = 1
    while count == 1:
        try:
            meses_trabalhados = int(input('Informe a quantidade de meses trabalhados: '))
        except ValueError:
            print(f'{RED}O MES precisa ser um numero inteiro positivo.{RESET}')
            pass
        else:
            if meses_lista.count(meses_trabalhados) == 2:
                print(f'{RED}Já existe 2 pessoas nesse mês, por favor tente outra quantidade.{RESET}')
                pass
            else:
                count = 0

    id_list.append(id_empregado)
    meses_lista.append(meses_trabalhados)

    if meses_trabalhados > antigo:
        antigo = meses_trabalhados
        id_antigo = id_empregado

    elif meses_trabalhados < recente:
        recente = meses_trabalhados
        id_recente = id_empregado

    print(f'\n{BOLD}RECENTE:{RESET}\nID do empregado: %04d' % id_recente, '\nMESES:', recente)
    print(f'\n{BOLD}ANTIGO:{RESET}\nID do empregado: %04d' % id_antigo, '\nMESES:', antigo)
