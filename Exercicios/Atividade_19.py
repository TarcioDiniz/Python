# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
# descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela
# abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas
# não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao
# Salário Bruto menos os descontos. O programa Python deverá pedir ao usuário o valor
# da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) — isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 — desconto de 20%
# Imprima na tela as informações a seguir. No exemplo o valor da hora é 5 e a
# quantidade de hora é 220.

# Salário Bruto: (5 * 220) : R$ 1100,00
# (-) IR (5%) : R$ 55,00
# (-) INSS ( 10%) : R$ 110,00
# FGTS (11%) : R$ 121,00
# Total de descontos : R$ 165,00
# Salário Liquido : R$ 935,00

try:
    valor_hora = float(input('Informe seu valor/hora: '))
except ValueError:
    print('Número não reconhecido.')
    exit()
if valor_hora < 0:
    print('Valor negativo.')
    exit()

try:
    total_hora = float(input('Informe o total de horas do mês: '))
except ValueError:
    print('Número não reconhecido.')
    exit()
if total_hora < 0:
    print('valor negativo.')
    exit()


salario_bruto = valor_hora * total_hora

_IR_ = salario_bruto * (5 / 100)  # desconta
_INSS_ = salario_bruto * (10 / 100)  # desconta
_FGTS_ = salario_bruto * (11 / 100)


print(f'Salário Bruto: R$ {salario_bruto}')
print(f'(-) IR (5%): R$ {_IR_}')
print(f'(-) INSS (10%): R$ {_INSS_}')
print(f'FGTS (11%): R$ {_FGTS_}')
print(f'Total de descontos: R$ {_IR_ + _INSS_}')
print(f'Salário Liquido: R$ {salario_bruto - (_IR_ + _INSS_)}')

