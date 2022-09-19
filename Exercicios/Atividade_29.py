# Desenvolver um programa em Python para calcular a conta de água para a
# CAGEPA. O custo da água varia dependendo se o consumidor é residencial,
# comercial ou industrial. A regra para calcular a conta é:
# — Residencial: R$50,00 de taxa mais R$0,05 por m³ gastos;
# – Comercial: R$500,00 para os primeiros 80 m³ gastos mais R$0,25 por m³
# gastos acima dos 80 m³; –
# Industrial: R$800,00 para os primeiros 100 m³
# gastos mais R$0,04 por m³
# gastos acima dos 100 m³;
# O programa deverá ler o número da conta do cliente, consumo de água por
# metros cúbicos e o tipo de consumidor (residencial, comercial e industrial).
# Como resultado, imprima o número da conta do cliente e o valor real a ser pago pelo mesmo.

print('Dessa lista, qual a categoria de consumidor você se encaixa?')

lista_consumidor = ['residencial', 'comercial', 'industrial']

for i in range(len(lista_consumidor)):
    print(f'{i} - {lista_consumidor[i]}')

while True:
    try:
        _tipo_consumidor = int(input('Digite aqui: '))
        if _tipo_consumidor < 0:
            print('Número negativo? kkkk')
            pass
        elif _tipo_consumidor > 2:
            print('Por favor, digite número entre 0 e 2')
            pass
        else:
            break
    except ValueError:
        print('Número não reconhecido.')
        print('Por favor, digite número entre 0 e 2')
        pass

while True:
    try:
        _gasto_metro_agua = float(input('Informe quantos m³ de água foi consumido: '))
        if _gasto_metro_agua < 0:
            print('Número negativo? kkkk')
            pass
        else:
            break
    except ValueError:

        print('Número não reconhecido.')
        pass
taxa_fixa = 0
taxa_metro = 0
total = 0

if _tipo_consumidor == 0:
    taxa_fixa = 50
    taxa_metro = 0.05
    total = taxa_fixa + (_gasto_metro_agua * taxa_metro)

elif _tipo_consumidor == 1:
    taxa_fixa = 500
    total = taxa_fixa
    if _gasto_metro_agua > 80:
        taxa_metro = 0.25
        total = taxa_fixa + (_gasto_metro_agua * taxa_metro)
elif _tipo_consumidor == 2:
    taxa_fixa = 800
    total = taxa_fixa
    if _gasto_metro_agua > 100:
        taxa_metro = 0.04
        total = taxa_fixa + (_gasto_metro_agua * taxa_metro)

print('O valor total foi: R$ %.2f' % total)