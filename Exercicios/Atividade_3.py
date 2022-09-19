# Faça um Programa Python que peça a temperatura em graus Farenheit, transforme e
# mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

while True:
    print('Converta Farenheit em Celsius.')
    graus_Farenheit = input('Digite um valor em graus Farenheit: ')
    try:
        print(eval(f'5 * ({graus_Farenheit}-32) / 9'), '°F', sep='')
        break
    except NameError:
        print('----------------------------')
        print('Por favor, digite um número.')
        print('----------------------------')
        pass
