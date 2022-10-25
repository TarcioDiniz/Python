# Escreva um programa em Python para converter um número inteiro em binário
# de acordo com a representação de grandeza com sinal (sinal e magnitude). O
# programa deve receber um número inteiro e produzir como saída uma lista com
# os bits do número convertido (um bit para cada posição da lista). Além disso
# deve ser feita a verificação se o número pode ser representado, considere uma
# representação com 8 bits (um para o sinal e 7 para a magnitude).

def decimalToBinary(decimal):  # Com 8 bits
    negativo = False
    if decimal < 0:
        decimal = decimal * -1
        negativo = True
    binario = ''
    while decimal > 0:
        binario += str(decimal % 2)
        decimal //= 2

    binario = list(binario[::-1])

    indice = 0

    if negativo:
        for i in range(1, 1 + len(binario)):
            if binario[i * -1] == '1':
                indice = -i
                break

        for i in range(len(binario) * -1, indice):
            if binario[i] == '1':
                binario[i] = '0'
            else:
                if binario[i] == '0':
                    binario[i] = '1'

        binario = '1 ' + ''.join(binario)

    else:
        binario = '0 ' + ''.join(binario)

    if len(list(binario)) > 9:
        return 'Overflow'

    return binario


print(decimalToBinary(100))
