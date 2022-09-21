# O IPVA é calculado de acordo com o tipo de veículo, cuja alíquota é definida por cada
# Estado sobre o valor venal do carro de acordo com a Tabela Fipe (Fundação Instituto
# de Pesquisas Econômicas), variando entre 1% e 4%. Escreva um programa em Python
# para calcular o valor do IPVA de um veículo com base nas informações a seguir:

# Alíquota ------------- Tipo do Veículo
# 4,0% ----------------- 'Automóveis' 0
# 3,0% ----------------- 'Caminhonetes de carga' e 'furgão'. 1 - 2
# 2,0% ----------------- 'Automóveis para transporte público (ex: táxi,escolar)' 3
# 2,0% ----------------- 'Motocicletas'. 4
# 1,0% ----------------- 'Veículos de locadoras'. 5
# 1,0% ----------------- 'Ônibus', 'micro-ônibus', 'caminhão', 'caminhão trator'. 6 - 9


print('Dessa lista, qual a categoria que seu veiculo se encaixa?\n')

tipo_veiculo = [
    'Automóveis',
    'Caminhonetes de carga',
    'furgão',
    'Automóveis para transporte público (ex: táxi,escolar)',
    'Motocicletas',
    'Veículos de locadoras',
    'Ônibus',
    'micro-ônibus',
    'caminhão',
    'caminhão trator'
]

for i in range(len(tipo_veiculo)):
    print(f'{i} - {tipo_veiculo[i]}')
while True:
    try:
        _input_tipo_veiculo = int(input('\nDigite aqui: '))
        if _input_tipo_veiculo < 0:
            print('Valor negativo? kkkk')
            pass
        elif _input_tipo_veiculo > 9:
            print('Apenas números de 0 a 9. Por favor.')
            pass
        else:
            break
    except ValueError:
        print('Apenas números correspondente na lista acima.')
        pass


while True:
    try:
        valor_carro = float(input('Informe o valor do carro: '))
        if valor_carro < 0:
            print('Valor negativo? kkkk')
            pass
        else:
            break
    except ValueError:
        print('Apenas números por favor.')
        pass

if _input_tipo_veiculo == 0:
    _IPVA_ = valor_carro * (4/100)
elif 1 <= _input_tipo_veiculo <= 2:
    _IPVA_ = valor_carro * (3 / 100)
elif 3 <= _input_tipo_veiculo <= 4:
    _IPVA_ = valor_carro * (2 / 100)
elif 5 <= _input_tipo_veiculo <= 9:
    _IPVA_ = valor_carro * (1 / 100)

print('Seu IPVA será: R$ %.2f' % _IPVA_)
