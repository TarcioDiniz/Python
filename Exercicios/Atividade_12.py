# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendose que
# são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o
# sindicato, faça um programa Python que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
# Salário Bruto : R$
# IR (11%) : R$
# INSS (8%) : R$
# Sindicato ( 5%) : R$
# Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


while True:
    print('Calcule seu Holerite')
    valor_hora = input('Digite quanto você ganha por hora: ')
    try:
        if eval(valor_hora) < 0:
            print('Você colocou um valor negativo')
            exit()
        num_hora = input('Digite o número de horas trabalhadas no mês: ')
        if eval(num_hora) < 0:
            print('Você colocou um valor negativo')
            exit()
    except NameError:
        pass

    try:
        salario_bruto = eval(f'{valor_hora} * {num_hora}')
        inss = (8/100) * salario_bruto
        sindicado = (5/100) * salario_bruto
        imposto_renda = (11/100) * salario_bruto
        salario_liquido = salario_bruto - inss - sindicado - imposto_renda

        print('Salário Bruto: R$', salario_bruto)
        print('IR (11%) : R$', imposto_renda)
        print('INSS (8%) : R$', inss)
        print('Sindicato ( 5%) : R$', sindicado)
        print('Salário Liquido : R$', salario_liquido)
        break
    except NameError:
        print('----------------------------')
        print('Por favor, digite um número.')
        print('----------------------------')
        pass



