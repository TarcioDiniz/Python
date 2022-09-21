# Elabore um programa Python que dada a idade de um nadador classifica-o em uma
# das seguintes categorias: infantil A = 5 - 7 anos; infantil B = 8-10 anos; juvenil A = 11-13 anos;
# juvenil B = 14-17 anos; adulto = maiores de 18 anos.

idade = int(input('Informe dua idade: '))

if idade < 0:
    print('idade negativa?')
    exit()
else:
    if idade < 5:
        print('Idade a partir de 5 anos.')
        exit()
    else:
        if idade >= 90:
            print('Tem certeza que essa é uma idade segura?')
            exit()

if 5 <= idade <= 7:
    print('Classificação infantil A = 5 - 7 anos;')
else:
    if 8 <= idade <= 10:
        print('Classificação infantil B = 8-10 anos')
    else:
        if 11 <= idade <= 13:
            print('Classificação juvenil A = 11-13 anos')
        else:
            if 14 <= idade <= 17:
                print('Classificação juvenil B = 14-17 anos')
            else:
                if idade >= 18:
                    print('Classificação adulto = maiores de 18 anos')