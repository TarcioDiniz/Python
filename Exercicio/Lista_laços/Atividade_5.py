# Faça um programa para calcular a área de N quadriláteros. Fórmula: Área = Lado * Lado.

numero = int(input('Infome a quatidade quadriláteos: '))

if numero < 0:
    print('Numero negativo.')
    exit()
for i in range(numero):
    lado = float(input(f'Infome o lado quadrilátero {i + 1}: '))
    print(f'Aréa: {lado * lado}')
