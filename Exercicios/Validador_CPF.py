def calculo(CPF_USER):
    LISTA_CPF = []
    for lista1 in range(9):
        LISTA_CPF.append(int(CPF_USER[lista1]))
    DIGITO = []
    for indexDI in range(10, 1, -1):
        DIGITO.append(indexDI)
    SOMA = 0
    for soma_CPF_DIG in range(9):
        SOMA += LISTA_CPF[soma_CPF_DIG] * DIGITO[soma_CPF_DIG]
    Total1 = 11 - (SOMA % 11)
    if Total1 > 9:
        LISTA_CPF.insert(10, 0)
        DIGITO.insert(0, 11)
    else:
        LISTA_CPF.insert(10, Total1)
        DIGITO.insert(0, 11)
    SOMA2 = 0
    for soma_CPF_DIG2 in range(10):
        SOMA2 += LISTA_CPF[soma_CPF_DIG2] * DIGITO[soma_CPF_DIG2]
    Total2 = 11 - (SOMA2 % 11)
    if Total2 > 9:
        LISTA_CPF.insert(11, 0)
    else:
        LISTA_CPF.insert(11, Total2)
    lista_compara = []
    for indexCompra in range(11):
        lista_compara.append(int(CPF_USER[indexCompra]))

    if set(lista_compara) == set(LISTA_CPF):
        print('Valido')
    else:
        print('invalido')


def pergunta(CPF):
    CPF_BRL = CPF
    if len(CPF_BRL) == 11 and CPF_BRL.isnumeric():
        calculo(CPF_BRL)

    elif '.' and '-' in CPF_BRL and len(CPF_BRL) == 14:
        Separa_ponto = CPF_BRL.split('.')
        separdor2 = ''.join(Separa_ponto).split('-')
        CPF_USER2 = ''.join(separdor2)
        calculo(CPF_USER2)
    else:
        print('CPF invalido.')
        return pergunta(input("Por Favor digite novamente: "))

print('Validador de CPF')
pergunta(input("Digite seu CPF: "))
