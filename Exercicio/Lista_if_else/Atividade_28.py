# Escreva um programa em Python para ler a capacidade de um elevador (em toneladas)
# e o peso total das pessoas em seu interior (em quilogramas). Informar se o elevador
# está liberado para subir ou se excedeu a carga máxima.

while True:
    try:

        capacidade = float(input('Digite a capacidade do elevador em toneladas: '))
        if capacidade < 0:
            print('Número negativo?? kkkkk')
            pass
        else:
            break
    except ValueError:
        print('Número não identificado.')
        pass

peso_pessoas = 0
contador = 0
while True:
    contador += 1
    while True:
        try:
            peso_pessoas += float(input(f'Peso da {contador}° pessoa: '))
            if peso_pessoas < 0:
                print('Número negativo?? kkkkk')
                pass
            else:
                break
        except ValueError:
            print('Número não identificado.')
            pass

    if peso_pessoas / 1000 >= capacidade:
        print('Limite de pessoas atingido.')
        print(f'Couberam {contador} pessoas.')
        break


