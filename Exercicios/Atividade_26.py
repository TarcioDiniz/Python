# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um
# programa Python que calcule seu peso ideal, utilizando as seguintes fórmulas: para
# homens: (72.7*h) – 58 e para mulheres: (62.1*h) - 44.7 (h = altura)

while True:
    try:
        altura = float(input('Digite sua altura: '))
    except ValueError:
        print('Número não identificado.')
        pass
    try:
        if altura < 0:
            print('Altura negativa? kkk')
            pass
        else:
            break
    except NameError:
        pass

peso_ideal = 0
while True:
    sexo = input('Qual seu sexo M | F: ').upper()

    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
        print(f'Seu peso ideal é: %.2f Kg' % peso_ideal)
        break
    else:
        if sexo == 'F':
            peso_ideal = (62.1 * altura) - 44.7
            print(f'Seu peso ideal é: %.2f Kg' % peso_ideal)
            break
        else:
            print('Escolha M para Masculino ou F para Feminino.')
