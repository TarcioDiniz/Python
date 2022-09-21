# Tendo como dados de entrada a altura de uma pessoa, construa um programa Python
# que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) – 58.

print('Calculo do peso ideal baseado na altura.')

while True:
    try:
        altura = float(input('Digite sua altura: '))
        if altura < 0:
            print('Você colocou um valor negativo')
            pass
        else:
            break
    except ValueError:
        print('----------------------------')
        print('Por favor, digite um número.')
        print('----------------------------')
        pass

print('Seu peso ideal é:', eval(f'(72.7 * {altura}) - 58'), 'Kg')


