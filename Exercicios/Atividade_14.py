# Na fazenda de João são criadas aves. Para alimentá-las ele compra sacas de ração cujo
# peso é fornecido em quilos. No total ele tem dois grupos de aves, para os quais
# fornece a quantidade de ração em gramas. A quantidade diária de ração fornecida
# para cada grupo de aves é sempre a mesma. Faça um programa em Python que receba
# o peso do saco de ração e a quantidade de ração fornecida para cada grupo de aves,
# calcule e mostre quanto restará de ração após uma semana.

try:
    _quilos_racao = float(input('Quantos quilogramas de ração você comprou? '))
    if _quilos_racao <= 0:
        print('Você digitou número negativo.')
        exit()
except ValueError:
    print('Você digitou uma letra')
    exit()
try:
    _quantidade_gramas_ave = float(input('Quantas gramas de ração as aves consome por dia? '))
    if _quantidade_gramas_ave <= 0:
        print('Você digitou número negativo.')
        exit()
except ValueError:
    print('Você digitou uma letra')
    exit()

if _quantidade_gramas_ave <= 0:
    print('Você digitou número negativo.')
    exit()

_dia_semana = 7

total = _quilos_racao - ((_quantidade_gramas_ave * 2) * _dia_semana)

if total < 0:
    print(f'Durante a semana faltará {total}Kg de ração.')
else:
    print(f'Após uma semana restará apenas {total}Kg de ração.')
