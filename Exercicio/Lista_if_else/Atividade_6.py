# Escrever um programa Python para determinar o consumo médio de um automóvel
# sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto.

while True:
    distancia = input('Distância pecorrida pelo automovel: ')
    if distancia.isdigit():
        break
    else:
        print('----------------------------')
        print('Por favor, digite um número.')
        print('----------------------------')

while True:
    litros_gasolina = input('Quantidade de litros de gasolina colocado no veiculo: ')
    if litros_gasolina.isdigit():
        break
    else:
        print('----------------------------')
        print('Por favor, digite um número.')
        print('----------------------------')

print('Seu veiculo consumiu: ', eval(f'{distancia} / {litros_gasolina}'), ' Km/L', sep='')
