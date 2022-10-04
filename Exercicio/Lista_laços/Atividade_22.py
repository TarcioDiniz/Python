# 22. Você foi contratado para escrever um algoritmo que calcule quantos pontos fez
# um time num campeonato de futebol. Para os que não conhecem futebol uma
# vitória vale três pontos, um empate vale 1 ponto e a derrota não vale ponto. A
# entrada será composta por pares de números indicando o resultado de cada
# jogo. O primeiro número sempre corresponde ao total de gols que o time fez no
# jogo. A leitura dos dados será finalizada quando for fornecido um número de
# gols negativo.

placar = 0
soma = 0
golsPro = int(input('Informe quanto GOLS seu time fez: '))
if golsPro < 0:
    print(f'Programa encerrado. Você fez um total de {soma} pontos')
else:
    golsContra = int(input('Informe quantos GOLS o time adversario fez: '))
    if golsContra < 0:
        print(f'Programa encerrado. Você fez um total de {soma} pontos')
    else:
        verifica = 1
        while verifica == 1:
            if golsPro > golsContra:
                print('Ganhou +3 pontos')
                soma += 3
            else:
                if golsPro == golsContra:
                    print('Empate. +1 ponto')
                    soma += 1
                else:
                    print('Derrota. 0 pontos')
                golsPro = int(input('Informe quanto GOLS seu time fez: '))
                if golsPro < 0:
                    verifica = 0
                else:
                    golsContra = int(input('Informe quantos GOLS o time adversario fez: '))
                    if golsContra < 0:
                        verifica = 0
        print(f'Programa encerrado. Você fez um total de {soma} pontos')
