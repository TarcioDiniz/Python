# Uma organização resolveu dar um aumento de salário aos seus colaboradores e lhe
# contrataram para desenvolver o programa que calculará os reajustes. Faça um
# programa Python que recebe o salário de um colaborador e o reajuste segundo o
# seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# a. o salário antes do reajuste;
# b. o percentual de aumento aplicado;
# c. o valor do aumento;
# d. o novo salário, após o aumento

try:
    salario = float(input('Digite seu salário: '))
    if salario < 0:
        print('Valor negativo.')
        exit()
except ValueError:
    print('Número não reconhecido.')
    exit()
salario_bruto = salario
if salario < 280:
    salario = salario + (salario * 20 / 100)
else:
    if 280 <= salario < 700:
        salario = salario + (salario * 15 / 100)
    else:
        if 700 <= salario < 1500:
            salario = salario + (salario * 10 / 100)
        else:
            if salario >= 1500:
                salario = salario + (salario * 5 / 100)

print(f'a. o salário antes do reajuste; {salario_bruto}')
print(f'b. o percentual de aumento aplicado; {((100 * salario) / salario_bruto) - 100}%')
print('c. o valor do aumento %.2f;' % (salario - salario_bruto))
print('d. o novo salário, após o aumento: %.2f' % salario)
