# Escrever um programa em Python que lê o público total de um jogo de futebol e
# fornecer a renda do jogo, sabendo-se que havia 4 tipos de ingressos assim distribuídos:
# popular 10% a R$10,00, geral 50% a R$50,00, arquibancada 30% a R$100,00 e cadeiras
# 10% a R$ 200,00.

print('Bem-vindo ao jogo de futebol')
try:
    publico = int(input('Informe a quantidade de ingressos vendidos: '))
except ValueError:
    print('Você digitou uma letra')
    exit()

if publico < 0:
    print('Você digitou um número negativo')
    exit()

_10_porcento = (10 / 100) * publico
_50_porcento = (50 / 100) * publico
_30_porcento = (30 / 100) * publico

_valor_popular = 10 * _10_porcento
_valor_geral = 50 * _50_porcento
_valor_arquibancada = 100 * _30_porcento
_valor_cadeiras = 200 * _10_porcento

total = _valor_popular + _valor_geral + _valor_arquibancada + _valor_cadeiras

print('Total arredado foi R$ %.0f' % total)
